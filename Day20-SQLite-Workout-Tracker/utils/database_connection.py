import sqlite3


class DatabaseConnection:
    def __init__(self, db_name='data.db'):
        self.db_name = db_name
        self.connection = None

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
        
    
    def __exit__(self, exc_type: type, exc_val:BaseException, exc_db: BaseException) -> None:
        if exc_type or exc_val or exc_db:
            self.connection.close()
            raise
        else:
            self.connection.commit()
            self.connection.close()

        