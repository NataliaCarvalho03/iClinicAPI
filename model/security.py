from .data_base import Data_Base
import os

class Security:

    database = Data_Base(os.getenv('db_address'))
    users = database.get_users_data()

    username_mapping = {u.username: u for u in users}
    userid_mapping = {u.id: u for u in users}

    def authenticate(self, username, password):
        user = self.username_mapping.get(username, None)
        if user and user.password == password:
            return user


    def identity(self, payload):
        user_id = payload['identity']
        return self.userid_mapping.get(user_id, None)


    def update_users(self):
        self.users = self.database.get_users_data()
        self.username_mapping = {u.username: u for u in self.users}
        self.userid_mapping = {u.id: u for u in self.users}
        print('Atualizei')
        print(self.users)