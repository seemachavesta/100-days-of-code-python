import sqlite3

# Handles database connections using a context manager.
# Ensures proper connection handling with automatic commit or rollback.
class DatabaseConnection:
    def __init__(self, db_name='data.db'):
        # Initialize the database name and set the connection to None.
        self.connection = None
        self.db_name = db_name

    def __enter__(self):
         # Open a connection to the database when entering the context.
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        #Commit changes if no exception occurs; otherwise, rollback and close the connection
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()