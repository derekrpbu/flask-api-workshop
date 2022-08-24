from db.mongo_client import Connection


class UserDBConnection:

    def __init__(self, collection):
        self.connection = Connection(collection)

    def create_data(self, data):
        response = self.connection.create_data(data)
        if type(response) is Exception:
            message = "Error: Something gone wrong trying to create a new user"
            return Exception(message)
        return response

    def update_data(self, id, user_updated_data):
        response = self.connection.update_data(id, user_updated_data)
        if type(response) is Exception:
            message = "Error: Something gone wrong trying to update the user"
            return Exception(message)
        return response

    def get_all_data(self):
        response = self.connection.get_all_data()
        if type(response) is Exception:
            message = "Error: Something gone wrong trying to get the user list"
            return Exception(message)
        return response

    def get_by_field(self, isActive):
        response = self.connection.get_by_field(isActive)
        if type(response) is Exception:
            message = "Error: Something gone wrong trying to get the user "
            return Exception(message)
        return response

    def delete_user(self, id):
        response = self.connection.delete_data(id)
        if type(response) is Exception:
            message = "Error: Something gone wrong trying to delete the user"
            return Exception(message)
        return response