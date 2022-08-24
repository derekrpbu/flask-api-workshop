from flask import Flask
from flask_restful import Api
from service import addServiceLayer
from decouple import config

app = Flask(__name__)
app.debug = config('FLASK_DEBUG', cast=bool)
api = Api(app)

addServiceLayer(api)

if __name__ == '__main__':
    app.run(host=config('FLASK_RUN_HOST'), port=config('BOOKSTORE_PORT'))


