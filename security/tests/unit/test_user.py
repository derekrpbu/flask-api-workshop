from unittest import TestCase

from models.user.user import User

class UserTest(TestCase):

    def test_create_item(self):
        user = User('1', 'derek', 'derek@test.com', '123', True)

        self.assertEqual(user.id[0], '1')
        self.assertEqual(user.userName[0], 'derek')
        self.assertEqual(user.email[0], 'derek@test.com')
        self.assertEqual(user.userPassword[0], '123')
        self.assertEqual(user.isActive[0], True)
