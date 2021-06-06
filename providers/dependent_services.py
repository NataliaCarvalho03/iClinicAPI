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


    def consult_services(self, ids: list):
        services_url = 'https://5f71da6964a3720016e60ff8.mockapi.io/v1'
        services = list(self.consult_services_auth.keys())
        services_responses = []
        for index in range(len(services)):
            self.header['Authorization'] = self.consult_services_auth[services[index]]
            services_responses.append(requests.request('GET', url=services_url + f'/{services[index]}/{ids[index]}', headers=self.header).json())
        return services_responses

    
    def post_metrics(self, responses_list: list):
        metrics_url = 'https://5f71da6964a3720016e60ff8.mockapi.io/v1/metrics'
        self.header['Authorization'] = self.metrics_auth
        metrics_payload = dict()
        metrics_payload['clinic_id'] = responses_list[1]['id']
        metrics_payload['clinic_name'] = responses_list[1]['name']
        metrics_payload['physician_id'] = responses_list[0]['id']
        metrics_payload['physician_name'] = responses_list[0]['name']
        metrics_payload['physician_crm'] = responses_list[0]['crm']
        metrics_payload['patient_id'] = responses_list[2]['id']
        metrics_payload['patient_name'] = responses_list[2]['name']
        metrics_payload['patient_email'] = responses_list[2]['email']
        metrics_payload['patient_phone'] = responses_list[2]['phone']
        resp = requests.request('POST', url=metrics_url, headers=self.header)
        print('METRICS STATUS: ', resp.status_code)
        return metrics_payload

