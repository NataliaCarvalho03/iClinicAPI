from .data_base import Data_Base
import os

class Security:

    __state={}

    def __new__(cls, *args, **kwargs):
        obj = super(Security, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = Security.__state
        return obj

    def __init__(self) -> None:
        self.database = Data_Base(os.getenv('db_address'))
        self.users = self.database.get_users_data()
        self.username_mapping = {u.username: u for u in self.users}
        self.userid_mapping = {u.id: u for u in self.users}

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