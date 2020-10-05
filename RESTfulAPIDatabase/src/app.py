from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from api.security import authenticate, identity

from api.store_api import *

app = Flask(__name__)
app.secret_key = 'komorek' # This is insecure change later
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)