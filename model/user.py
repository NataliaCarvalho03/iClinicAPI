class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    
    def __repr__(self) -> str:
        rep = f'User (name: {self.username}, id: {self.id})'
        return rep