from db.user_db_connection import UserDBConnection
from decouple import config
from utils.commons import Commons

connection = UserDBConnection(config("USERS_COLLECTION"))


class User:
    id = "",
    userName = "",
    email = "",
    userPassword = "",
    isActive = True,

    def __init__(
            self,
            id,
            userName,
            email,
            userPassword,
            isActive
    ):
        self.id = id,
        self.userName = userName,
        self.email = email,
        self.userPassword = userPassword,
        self.isActive = isActive,

    @classmethod
    def get_by_field(self, isActive):
        list_to_return = Commons.convertIds(list(connection.get_by_field(isActive)))
        return list_to_return

    @classmethod
    def get_all(self):
        list_to_return = Commons.convertIds(list(connection.get_all_data()))

        return list_to_return

    def create_user(self):
        new_user = {
            'id': self.id[0],
            'userName': self.userName[0],
            'email': self.email[0],
            'userPassword': self.userPassword[0],
            'isActive': self.isActive[0],
        }
        return connection.create_data(new_user)

    def update(self, id):
        return connection.update_data(id, {
            'userName': self.userName[0],
            'userPassword': self.userPassword[0],
        })

    @classmethod
    def delete(self, id):
        return connection.delete_user(id)
