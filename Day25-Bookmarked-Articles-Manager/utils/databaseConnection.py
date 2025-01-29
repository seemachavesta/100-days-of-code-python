import sqlite3


class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            return self.connection
        except sqlite3.Error as e:
            print(f"An error occurred while connecting to the database: {e}")
            raise
            
    
    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self, 'connection'):
            self.connection.close()
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred: {exc_value}")
    
  


    