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


if __name__ == '__main__':
    unittest.main()
