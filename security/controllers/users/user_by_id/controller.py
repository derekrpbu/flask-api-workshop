from models.user.user import User
from flask_restful import Resource, request
from utils.responses import CodeResponses
from models.user.user import User as UserModel


class UserById(Resource):
    route = '/users/<id>'

    def get(self, id):
        print(id)

        req = request.get_json()
        isActive = req['isActive']

        data = UserModel.get_by_field(isActive)

        if len(data) < 1:
            return CodeResponses.customResponse({"message": "Couldn't found Users", "status": 200, "data": None}, None)

        return CodeResponses.successfullyResponse(None, data)

    def delete(self, id):
        data = UserModel.delete(id)

        if data.deleted_count == 0:
            return CodeResponses.customResponse({"message": "Couldn't found User", "status": 200, "data": None}, None)

        return CodeResponses.deletedResponse(None)

    def put(self, id):
        data = request.get_json()
        data['id'] = id
        updated_user = UserModel(**data)

        print(updated_user.id)

        response = updated_user.update(id)
        if type(response) is Exception:
            return CodeResponses.InternalServerErrorResponse(None, str(response))

        return CodeResponses.updatedResponse(None, data)