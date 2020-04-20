import unittest
import json
import sql_server

from sql_server import app

class Test(unittest.TestCase):
    def setUp(self):
        self.appx = app.test_client()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_get_tasks_status(self):
        rv = self.appx.get('/tasks/1')
        self.assertEqual(rv.status, '200 OK')

    def test_get_tasks_resp(self):
        rv = self.appx.get('/tasks/1')
        data = rv.data
        data = b'{"result":[{"answer":"549","challengeid":1,"description":"Add two numbers: 234 + 315","id":1,"title":"Add"},{"answer":"70","challengeid":1,"description":"24 + 15 * 4 - (12 + 2) = ?)","id":2,"title":"Simple calculus"},{"answer":"4","challengeid":1,"description":"(-2) * 2","id":3,"title":"This is fast"},{"answer":"17","challengeid":1,"description":"7th prime number?","id":4,"title":"Easy one"}]}\n'
        self.assertEqual(data, rv.data)

    def test_get_tasks_status2(self):
        rv = self.appx.get('/tasks/2')
        self.assertEqual(rv.status, '200 OK')

    def test_get_tasks_status3(self):
        rv = self.appx.get('/tasks/3')
        self.assertEqual(rv.status, '200 OK')

    def test_get_challenges_status(self):
        rv = self.appx.get('/challenges')
        self.assertEqual(rv.status, '200 OK')

    def test_get_challenges_resp(self):
        rv = self.appx.get('/challenges')
        data = json.loads(rv.data)
        l = len(data['result'])
        elem = data['result'][0]
        res = {'description': 'This is to get familiar with the platform', 'difficulty': 1, 'id': 1, 'title': 'WarmUp', 'xp': 10}
        self.assertEqual(l, 17)
        self.assertEqual(elem, res)

    def test_get_stats_status(self):
        rv = self.appx.post('/stats', json={'userid': '1'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_stats_resp(self):
        rv = self.appx.post('/stats', json={'userid': '1'})
        data = json.loads(rv.data)
        d = {'result': {'level': 7,
            'names': ['WarmUp',
                      'Crypto',
                      'Example',
                      'Hacker',
                      'Paris',
                      'Harry Potter',
                      'Math'],
            'stars': 20,
            'xp': 540}}
        self.assertEqual(data, d)

    def test_get_stats_status2(self):
        rv = self.appx.post('/stats', json={'userid': '2'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_stats_resp2(self):
        rv = self.appx.post('/stats', json={'userid': '2'})
        data = json.loads(rv.data)
        d = {'result': {'level': 1, 'names': ['WarmUp'], 'stars': 1, 'xp': 10}}
        self.assertEqual(data, d)

    def test_get_stats_status3(self):
        rv = self.appx.post('/stats', json={'userid': '3'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_stats_resp3(self):
        rv = self.appx.post('/stats', json={'userid': '3'})
        data = json.loads(rv.data)
        d = {'result': {'level': 1, 'names': [], 'stars': 0, 'xp': 0}}
        self.assertEqual(data, d)

    def test_get_answer_status(self):
        rv = self.appx.post('/answer', json={'userid': '1', 'taskid': '1', 'answer': '100'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_answer_resp(self):
        rv = self.appx.post('/answer', json={'userid': '1', 'taskid': '1', 'answer': '100'})
        data = json.loads(rv.data)
        ans = {'result': {'answer': 0}}
        self.assertEqual(data, ans)

    def test_get_answer_status2(self):
        rv = self.appx.post('/answer', json={'userid': '2', 'taskid': '2', 'answer': '100'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_answer_resp3(self):
        rv = self.appx.post('/answer', json={'userid': '1', 'taskid': '2', 'answer': '100'})
        data = json.loads(rv.data)
        ans = {'result': {'answer': 0}}
        self.assertEqual(data, ans)

    def test_get_answer_status3(self):
        rv = self.appx.post('/answer', json={'userid': '1', 'taskid': '2', 'answer': '100'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_answer_resp2(self):
        rv = self.appx.post('/answer', json={'userid': '2', 'taskid': '2', 'answer': '100'})
        data = json.loads(rv.data)
        ans = {'result': {'answer': 0}}
        self.assertEqual(data, ans)

    def test_get_chanswer_status(self):
        rv = self.appx.post('/chanswer', json={'userid': '1', 'challengeid': '1', 'answer': '100'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_chanswer_resp(self):
        rv = self.appx.post('/chanswer', json={'userid': '1', 'challengeid': '1', 'answer': 'abc'})
        data = json.loads(rv.data)
        ans = {'result': {'answer': 0}}
        self.assertEqual(data, ans)

    def test_get_chanswer_resp2(self):
        rv = self.appx.post('/chanswer', json={'userid': '1', 'challengeid': '1', 'answer': '123'})
        data = json.loads(rv.data)
        ans = {'result': {'answer': 1}}
        self.assertEqual(data, ans)

    def test_get_chanswer_resp3(self):
        rv = self.appx.post('/chanswer', json={'userid': '2', 'challengeid': '1', 'answer': '123'})
        data = json.loads(rv.data)
        ans = {'result': {'answer': 1}}
        self.assertEqual(data, ans)


    def test_get_login_status(self):
        rv = self.appx.post('/users/login', json={'email': 'x@x.com', 'password': '1234'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_login_resp(self):
        rv = self.appx.post('/users/login', json={'email': 'x@x.com', 'password': '1234'})
        self.assertNotEqual(None, rv.data)

    def test_get_login_resp2(self):
        rv = self.appx.post('/users/login', json={'email': 'a@a.com', 'password': '1111'})
        self.assertNotEqual(None, rv.data)

    def test_get_register_status(self):
        rv = self.appx.post('/users/register', json={'email': 'x@x.com', 'username': 'abc'})
        self.assertEqual(rv.status, '200 OK')

    def test_get_registers_resp(self):
        rv = self.appx.post('/users/register', json={'email': 'x@x.com', 'username': 'abc'})
        data = json.loads(rv.data)
        res = {"result": {"email":"*", "username":"abc"}}
        self.assertEqual(res, data)

    def test_get_registers_resp2(self):
        rv = self.appx.post('/users/register', json={'email': 'a@a.com', 'username': 'name'})
        data = json.loads(rv.data)
        res = {"result": {"email":"*", "username":"name"}}
        self.assertEqual(res, data)

    def test_get_top(self):
        res = sql_server.get_top()
        l = res['result']
        is_reversed = True
        for i in range(len(l) - 1):
            if l[i][1] < l[i+1][1]:
                is_reversed = False
        self.assertTrue(is_reversed)

    def test_calculate_level_1(self):
        level = sql_server.calculate_level(0)
        self.assertEqual(level, 0)
        level = sql_server.calculate_level(5)
        self.assertEqual(level, 1)
        level = sql_server.calculate_level(300)
        self.assertEqual(level, 5)
        level = sql_server.calculate_level(324)
        self.assertEqual(level, 5)
        level = sql_server.calculate_level(325)
        self.assertEqual(level, 6)
        level = sql_server.calculate_level(1000)
        self.assertEqual(level, 9)



if __name__ == '__main__':
    unittest.main()