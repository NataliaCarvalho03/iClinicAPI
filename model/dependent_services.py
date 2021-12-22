import requests, os

class Dependent_Services():

    header = {
        'Content-Type': 'application/json',
        'Authorization': None
    }
    
    consult_services_auth = {
        'physicians': os.getenv('physicians'),
        'clinics': os.getenv('clinics'),
        'patients': os.getenv('patients'),
    }
    metrics_auth = os.getenv('metrics')

    services_url = 'https://5f71da6964a3720016e60ff8.mockapi.io/v1/'


    def consult_physicians(self, physician_id):
        self.header['Authorization'] = self.consult_services_auth['physicians']
        physicians_response = requests.request('GET', url=self.services_url + f'physicians/{physician_id}', headers=self.header)
        physicians_response=physicians_response.json()
        return physicians_response

    def consult_clinics(self, clinic_id):
        self.header['Authorization'] = self.consult_services_auth['clinics']
        clinics_response = requests.request('GET', url=self.services_url + f'clinics/{clinic_id}', headers=self.header)
        clinics_response=clinics_response.json()
        return clinics_response

    def consult_patients(self, patient_id):
        self.header['Authorization'] = self.consult_services_auth['clinics']
        clinics_response = requests.request('GET', url=self.services_url + f'patients/{patient_id}', headers=self.header)
        clinics_response=clinics_response.json()
        return clinics_response


    def consult_services(self, data: dict):
        physicians_resp = self.consult_physicians(data['physician']['id'])
        clinics_resp = self.consult_clinics(data['clinic']['id'])
        patients_resp = self.consult_patients(data['clinic']['id'])
        metrics_payload, metrics_response = self.post_metrics(physicians_resp, clinics_resp, patients_resp, data['text'])
        return [metrics_payload, metrics_response]

    
    def post_metrics(self, physician, clinic, patient, prescription):
        metrics_url = 'https://5f71da6964a3720016e60ff8.mockapi.io/v1/metrics'
        self.header['Authorization'] = self.metrics_auth
        metrics_payload = dict()
        metrics_payload['clinic_id'] = clinic['id']
        metrics_payload['clinic_name'] = clinic['name']
        metrics_payload['physician_id'] = physician['id']
        metrics_payload['physician_name'] = physician['name']
        metrics_payload['physician_crm'] = physician['crm']
        metrics_payload['patient_id'] = patient['id']
        metrics_payload['patient_name'] = patient['name']
        metrics_payload['patient_email'] = patient['email']
        metrics_payload['patient_phone'] = patient['phone']
        resp = requests.request('POST', url=metrics_url, headers=self.header)
        print('METRICS STATUS: ', resp.status_code)
        metrics_payload['prescription_text'] = prescription
        return [metrics_payload, resp]

