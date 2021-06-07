import sqlite3, os

class Data_Base():
    
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
            userid text,
            clinic_name text,
            physician_id text,
            physician_name text,
            physician_crm text,
            patient_id text,
            patient_name text,
            patient_email text,
            patient_phone text)""")
        self.connection.commit()
        self.connection.close()
    
    
    def get_user_data(self, username):
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        #my code here
        self.connection.close()
    

    def get_user_prescriptions(self, user_id):
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        #my code here
        self.connection.close()
    
    def create_new_user(self, user_id, username, password):
        self.connection = sqlite3.connect(self.db_address)
        self.cursor = self.connection.cursor()
        #my code here
        self.connection.commit()
        self.connection.close()
