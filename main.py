from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from flasgger import Swagger, swag_from
from dotenv import find_dotenv, load_dotenv
import os

from security import authenticate, identity
from providers.dependent_services import Dependent_Services

load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = os.getenv('api_key')
app.config["SWAGGER"] = {
    "title": "iClinic API",
    "description": """Prescriptions API for patient management.""",
    "openapi": "3.0.2",
}
jwt = JWT(app, authenticate, identity)
Swagger(app)
api = Api(app)

class Prescription(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clinic', type=dict, required=True)
    parser.add_argument('physician', type=dict, required=True)
    parser.add_argument('patient', type=dict, required=True)
    parser.add_argument('text', type=str, required=True)
    
    @jwt_required()
    @swag_from('docs/prescriptions.yaml')
    def post(self):
        data = self.parser.parse_args()
        services = Dependent_Services()
        serv_resp = services.consult_services([data['physician']['id'], data['clinic']['id'], data['patient']['id']])
        return services.post_metrics(serv_resp)

api.add_resource(Prescription, '/prescriptions')

if __name__ == '__main__':
    app.run(debug=True)