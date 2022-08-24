from flask_restful import Resource, request
from utils.responses import CodeResponses
from models.book.book import Book as BookModel

class Book(Resource):
    route = '/books/'
        
    def get(self):
        if 'title' in request.args:
            data = BookModel.get_by_name(request.args['title'])
        elif 'book_key' in request.args:
            data = BookModel.get_book_by_key(request.args['book_key'])
        if len(data) < 1:
            return CodeResponses.customResponse({"message": "Couldn't found Users", "status": 200, "data": None}, None)
            
        return CodeResponses.successfullyResponse(None, data)

