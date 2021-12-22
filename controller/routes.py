from view.resources import Prescription, Sign_Up

def get_routes():
    return [
        (Prescription, '/prescriptions'),
        (Sign_Up, '/signup'),
    ]