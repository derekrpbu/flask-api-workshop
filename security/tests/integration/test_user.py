from unittest import TestCase
from models.user.user import User
import mongomock
from db.user_db_connection import UserDBConnection

class TestUser(TestCase):

    #Models
    def test_get_all_users(self):
        self.assertIsNotNone(User.get_all())

    def test_create_user(self):
        pass

    def test_update_user(self):
        pass

    def test_delete_user(self):
        pass

    #Controllers
