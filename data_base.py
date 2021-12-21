import sqlite3, os
from user import User

class DataBaseMeta(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(DataBaseMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class Data_Base(metaclass=DataBaseMeta):
    
    connection = None
    cursor = None
    db_address = None


    def __init__(self, db_address) -> None:
        self.db_address = db_address
        db_exists = os.path.isfile(db_address)
        if not db_exists:
            self.connection = sqlite3.connect(self.db_address)
            self.cursor = self.connection.cursor()
            self.create_tables()

    
    def create_tables(self):
        self.cursor.execute('''CREATE TABLE users (userid text, username text, userpassword text)''')
        self.cursor.execute("""CREATE TABLE prescription (
            clinic_id text,
            clinic_name text,
            physician_id text,
            physician_name text,
            physician_crm text,
            patient_id text,
            patient_name text,
            patient_email text,
            patient_phone text,
            prescription_text text)""")
        self.connection.commit()
        self.connection.close()
    
    def insert_new_prescription(self, prescription_data: dict):
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        self.cursor.execute(" INSERT INTO prescription VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
                            (
                                prescription_data['clinic_id'],
                                prescription_data['clinic_name'],
                                prescription_data['physician_id'],
                                prescription_data['physician_name'],
                                prescription_data['physician_crm'],
                                prescription_data['patient_id'],
                                prescription_data['patient_name'],
                                prescription_data['patient_email'],
                                prescription_data['patient_phone'],
                                prescription_data['prescription_text']
                            ))
        self.connection.commit()
        print('Escrevi no banco')
        self.connection.close()
    
    def get_user_data(self, username):
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        #my code here
        self.connection.close()
    
    def get_users_data(self):
        all_users = []
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        users_info = self.cursor.execute(" SELECT * FROM users ")
        users_info = users_info.fetchall()
        for user in users_info:
            all_users.append(User(user[0], user[1], user[2]))
        self.connection.close()
        return all_users

    def get_user_prescriptions(self, user_id, username):
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        self.connection.close()
    
    def verify_user_existence(self, user_id, username):
        users_info = self.cursor.execute(" SELECT userid, username FROM users ")
        users_info = users_info.fetchall()
        for user_info in users_info:
            if (username == user_info[1]):
                return True
        return False

    
    def create_new_user(self, user_id, username, userpassword):
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        user_exists = self.verify_user_existence(user_id, username)
        if not user_exists:
            self.cursor.execute(" INSERT INTO users VALUES (?, ?, ?) ", (user_id, username, userpassword))
            self.connection.commit()
            self.connection.close()
            return ['user registered', 200]
        return ['username already in use. Please, consider enter another user name.', 200]
