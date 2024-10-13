import unittest
from unittest.mock import patch
from unit_testing.user_service import UserService
from unit_testing.custom_errors import RequestError
import os
from os.path import isfile

"""
inheriting unittest.Testcase will give us methods to
test a condition, create mocks and perofrm actions
before and after running tests.
"""
class TestUserService(unittest.TestCase):
    def setUp(self):
        self.mock_data =  '[{"id": 1, "name": "John Doe", "username": "john_doe", "phone": "+1234567890", "email": "johndoe@example.com"}]'
    def tearDown(self):
        files = ["test.csv", "test.json"]
        for file in files:
            if isfile(file):
                os.remove(file)
    def test_pull_all_users_success_response(self):
        with patch('user_service.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = self.mock_data
            pull_response = UserService.pull_all_users()
            self.assertEqual(pull_response, mocked_get.return_value.text)
    @unittest.skip
    def test_pull_all_users_failure_response(self):
        with patch('user_service.requests.get') as mocked_get:
            mocked_get.return_value.ok = False
            with self.assertRaises(RequestError) as exception_context:
                UserService.pull_all_users()
            self.assertEqual(str(exception_context.exception), 'Request is not successful.')
    
    def test_save_users_to_file_for_csv(self):
            UserService.save_users_to_file('test.csv', 'csv')
            self.assertTrue(isfile('test.csv'))
    def test_save_users_to_file_for_json(self):
            UserService.save_users_to_file('test.json', 'json')
            self.assertTrue(isfile('test.json'))




 
