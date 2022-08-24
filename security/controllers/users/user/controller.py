from flask_restful import Resource, request
from utils.responses import CodeResponses
from models.user.user import User as UserModel


class User(Resource):
    route = '/users'

    def get(self):
        data = UserModel.get_all()

        if len(data) < 1:
            return CodeResponses.customResponse({"message": "Couldn't found Users", "status": 200, "data": None}, None)

        return CodeResponses.successfullyResponse(None, data)


    # TODO: Field required validation
    def post(self):
        data = request.get_json()

        new_user = UserModel(**data)

        # Save to DB
        response = new_user.create_user()
        if type(response) is Exception:
            return CodeResponses.InternalServerErrorResponse(None, str(response))

        return CodeResponses.createdResponse(None, data)