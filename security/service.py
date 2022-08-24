from flask_restful import Resource
from utils.responses import CodeResponses
from controllers.users.user.controller import User as UserController
from controllers.users.user_by_id.controller import UserById as UserByIdController


class Status(Resource):
    route = "/bookstore/status"

    def get(self):
        return CodeResponses.statusOnline(None)


def addServiceLayer(api):
    api.add_resource(Status, Status.route)
    api.add_resource(UserController, UserController.route)
    api.add_resource(UserByIdController, UserByIdController.route)
