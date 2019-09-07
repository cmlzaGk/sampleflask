import unittest
import json
from randomweb_app import create_app

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.post('/betterrandomservice')
        self.assertEqual(response.status_code, 200)
        json_output = json.loads(response.get_data(as_text=True))
        self.maxDiff = None
        self.assertTrue(json_output['random_int'] >= 0 \
                            and json_output['random_int'] <= 10)
