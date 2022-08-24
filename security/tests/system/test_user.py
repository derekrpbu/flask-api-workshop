from unittest import TestCase
from models.user.user import User
from app import app
from flask import json


class UserTest(TestCase):
    def test_get_users(self):
        with app.test_client() as c:
            resp = c.get('/users')

            self.assertEqual(resp.status_code, 200)

    def test_create_user(self):
        new_user = {
            'id': 1,
            'userName': 'derek',
            'email': 'derek@test.com',
            'userPassword': '123',
            'isActive': True,
        }

        with app.test_client() as c:
            resp = c.post('/users', data=json.dumps(new_user), content_type='application/json')
            self.assertEqual(resp.status_code, 201)