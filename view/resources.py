from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flasgger import swag_from
import os

from model.security import Security
from model.dependent_services import Dependent_Services
from model.data_base import Data_Base

db = Data_Base(os.getenv('db_address'))

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
        serv_resp, metrics_resp = services.consult_services(data)
        db.insert_new_prescription(serv_resp)
        return 'ok', 200 #services.post_metrics(serv_resp)

class Sign_Up(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', type=str, required=True)
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('userpassword', type=str, required=True)

    def post(self):
        user_data = self.parser.parse_args()
        response = db.create_new_user(user_data['user_id'], user_data['username'], user_data['userpassword'])
        security=Security()
        print('Security at resources: ', security.username_mapping)
        security.update_users()
        return response[0], response[1]