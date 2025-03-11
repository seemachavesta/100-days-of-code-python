import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.connection = None
        self.db_name = db_name


    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
            