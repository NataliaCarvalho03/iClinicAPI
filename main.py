from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from flasgger import Swagger, swag_from
from dotenv import find_dotenv, load_dotenv
import os
from model.security import Security
from model.data_base import Data_Base
#from controller.routes import get_routes
from view.resources import Prescription, Sign_Up



load_dotenv(find_dotenv())
db = Data_Base(os.getenv('db_address'))
security=Security()
app = Flask(__name__)
app.secret_key = os.getenv('api_key')
app.config["SWAGGER"] = {
    "title": "iClinic API",
    "description": """Prescriptions API for patient management.""",
    "openapi": "3.0.2",
}
jwt = JWT(app, security.authenticate, security.identity)

Swagger(app)
api = Api(app)

api.add_resource(Prescription, '/prescriptions')
api.add_resource(Sign_Up, '/signup')

if __name__ == '__main__':
    app.run(debug=True)