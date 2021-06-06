import sqlite3, os

class Data_Base():
    def __init__(self, db_path) -> None:
        db_exists = os.path.isfile(db_path)
        self.connection = sqlite3.connect(db_path)
        if not db_exists:
            self.create_tables()
    
    
    def create_tables(self):
        pass
