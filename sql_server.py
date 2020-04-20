import mysql.connector as mariadb
from flask import Flask, jsonify, request, json
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret'

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

mydb = mariadb.connect(user='root', database='challenge_db')
mycursor = mydb.cursor()


def calculate_level(xp):
	if xp < 1:
		return 0
	elif xp < 20:
		return 1
	elif xp < 50:
		return 2
	elif xp < 100:
		return 3
	elif xp < 200:
		return 4
	elif xp < 325:
		return 5
	elif xp < 500:
		return 6
	elif xp < 725:
		return 7
	elif xp < 1000:
		return 8
	return 9  



@app.route('/top', methods=['GET', 'POST'])
def get_top():
	
	mycursor.execute("SELECT * FROM Solvedchallenges")
	rv = mycursor.fetchall()
	d = {}
	for x in rv:
		if x[1] in d:
			d[x[1]] += 1
		else:
			d[x[1]] = 1
	l = []
	for k, v in d.items():
		l.append([k, v])
	l.sort(key=lambda x: x[1], reverse=True)

	ans = []
	for x in l:
		userid = x[0]
		mycursor.execute("SELECT * FROM Users WHERE userid = '%s' " %(str(userid)))
		rv2 = mycursor.fetchone()
		ans.append([rv2[1], x[1]])

	result = {'result': ans}

	return result



@app.route('/taskanswer', methods=['GET', 'POST'])
def get_task_answer():
	print (request.get_json())
	print ('pppppppppppppppppppppppp')
	tid = request.get_json()['taskid']
	
	mycursor.execute("SELECT * FROM Tasks WHERE taskid = '%s' " %(str(tid)))
	rv2 = mycursor.fetchone()
	ans = rv2[3]
	print ('*******************')
	print (ans)

	result = {'result': ans}

	return result


@app.route('/solved_tasks', methods=['GET', 'POST'])
def get_solved_tasks():
	userid = request.get_json()['userid']
	mycursor.execute("SELECT * FROM Solvedtasks WHERE idUser = '%s' " %(str(userid)))
	rv = mycursor.fetchall()
	stasks = [x[2] for x in rv]
	result = {'result': stasks}

	return result


@app.route('/solved_challenges', methods=['GET', 'POST'])
def get_solved_challenges():
	userid = request.get_json()['userid']
	mycursor.execute("SELECT * FROM Solvedchallenges WHERE idUser = '%s' " %(str(userid)))
	rv = mycursor.fetchall()
	schallenges = [x[2] for x in rv]
	result = {'result': schallenges}

	return result


@app.route('/stats', methods=['GET', 'POST'])
def get_stats():
	print (request.get_json())
	print (request.args)
	userid = request.get_json()['userid']
	mycursor.execute("SELECT * FROM Solvedchallenges WHERE idUser = " + str(userid))
	rv = mycursor.fetchall()
	chs = [x[2] for x in rv]
	print (chs)
	xp = 0
	stars = 0
	level = 1
	names = []
	mycursor.execute("SELECT * FROM Challenges")
	rv = mycursor.fetchall()
	for x in rv:
		if x[0] in chs:
			xp += x[4]
			stars += x[3]
			names.append(x[1])
	if xp < 25:
		level = 1
	elif xp < 50:
		level = 2
	elif xp < 100:
		level = 3
	elif xp < 200:
		level = 4
	elif xp < 350:
		level = 5
	elif xp < 500:
		level = 6
	elif xp < 700:
		level = 7
	elif xp < 1000:
		level = 8
	else:
		level = 9

	result = {
			'xp': xp,
			'stars': stars,
			'level': level,
			'names': names
		}


	return jsonify({'result': result})


@app.route('/tasks/<chid>', methods=['GET'])
def get_tasks(chid):
    print (chid)
    id = chid
    mycursor.execute("SELECT * FROM Tasks WHERE challangeid = " + str(id))
    rv = mycursor.fetchall()
    print (rv)
    l = []
    for x in rv:
        l.append({'id': x[0],
            'title': x[1],
            'description': x[2],
            'answer': x[3],
            'challengeid': x[4]})


    return jsonify({'result': l})



@app.route('/challenges', methods=['GET'])
def get_challenges():

    mycursor.execute("SELECT * FROM Challenges")
    rv = mycursor.fetchall()
    print (rv)
    l = []
    for x in rv:
        l.append({'id': x[0],
            'title': x[1],
            'description': x[2],
            'difficulty': x[3],
            'xp': x[4]
            })

    return jsonify({'result': l})




@app.route('/answer', methods=['GET', 'POST'])
def get_answer():
	print (request.get_json())
	userid = request.get_json()['userid']
	taskid = request.get_json()['taskid']
	ans = request.get_json()['answer']
	mycursor.execute("SELECT * FROM Tasks WHERE taskid = " + str(taskid))
	rv = mycursor.fetchall()
	answer = rv[0][3]
	if (answer == ans):
		mycursor.execute("SELECT * FROM Solvedtasks WHERE idUser = '%s' and idTask = '%s'" %(str(userid), str(taskid)) )
		rv = mycursor.fetchall()
		print ('->', rv)
		if (len(rv) == 0):
			sql = "INSERT INTO Solvedtasks (idUser, idTask) \
			VALUES ('" + str(userid) + "','" + str(taskid) + "')"
			mycursor.execute(sql)
			mydb.commit()
			result = {
				'answer': 1
			}
		else:
			result = {
				'answer': 0
			}
	else:
		result = {
			'answer': 0
		}


	return jsonify({'result': result})

@app.route('/chanswer', methods=['GET', 'POST'])
def get_chanswer():
	print (request.get_json())
	userid = request.get_json()['userid']
	taskid = request.get_json()['challengeid']
	ans = request.get_json()['answer']
	mycursor.execute("SELECT * FROM Challenges WHERE challengeid = " + str(taskid))
	rv = mycursor.fetchall()
	answer = rv[0][5]
	if (answer == ans):
		mycursor.execute("SELECT * FROM Solvedchallenges WHERE idUser = '%s' and idChallenge = '%s'" %(str(userid), str(taskid)) )
		rv = mycursor.fetchall()
		print ('->', rv)
		if (len(rv) == 0):
			sql = "INSERT INTO Solvedchallenges (idUser, idChallenge) \
			VALUES ('" + str(userid) + "','" + str(taskid) + "')"
			mycursor.execute(sql)
			mydb.commit()
			result = {
				'answer': 1
			}
		else:
			result = {
				'answer': 1
			}
	else:
		result = {
			'answer': 0
		}


	return jsonify({'result': result})


@app.route('/users/register', methods=['POST'])
def register():
    username = request.get_json()['username']
    email = request.get_json()['email']

    mycursor.execute("SELECT * FROM Users where email = '" + str(email) + "'")
    rv = mycursor.fetchone()
    if rv != None:
        result = {
        'username': username,
        'email': '*'
        }
        return jsonify({'result': result})

    password = request.get_json()['password']
    
    sql = "INSERT INTO Users (username, password, email) \
    	VALUES ('" + str(username) + "','" + str(password) + "','" + str(email) + "')"
    mycursor.execute(sql)
    mydb.commit()

    result = {
        'username': username,
        'email': email
        }

    return jsonify({'result': result})


@app.route('/users/login', methods=['POST'])
def login():
	print ('ok')
	email = request.get_json()['email']
	password = request.get_json()['password']
	result = None

	mycursor.execute("""
		SELECT
		userid, username, password, email
		FROM
		Users
		WHERE
		email = %(uemail)s
		""", {
		'uemail': email
		})

	rv = mycursor.fetchone()

	if rv == None or len(rv[2]) == 0:
	    return result


	mycursor.execute("SELECT * FROM Solvedtasks WHERE idUser = '%s' " %(str(rv[0])))
	rv2 = mycursor.fetchall()
	stasks = [x[2] for x in rv2]

	mycursor.execute("SELECT * FROM Solvedchallenges WHERE idUser = '%s' " %(str(rv[0])))
	rv2 = mycursor.fetchall()
	schallenges = [x[2] for x in rv2]

	print ('***', schallenges)


	if rv[2] == password:
		access_token = create_access_token(
			identity={
				'userid': str(rv[0]),
				'username': rv[1],
				'email': rv[3],
				'stasks': stasks,
				'schallenges': schallenges
			})
		result = access_token
	else:
		result = None

	return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)