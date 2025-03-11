from utils.database_connection import DatabaseConnection


class Database:
    def __init__(self, db_name="data.db"):
        self.db_name = db_name

    def create_table(self):
        with DatabaseConnection(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    due_date TEXT,
                    priority TEXT
                )
            """)
            connection.commit()

            

    def insert_task(self, task):
        query = """INSERT INTO tasks (title, description, due_date, priority) 
                VALUES (?, ?, ?, ?)"""
        
        with DatabaseConnection(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (task.title, task.description, task.due_date, task.priority))
          


    def fetch_all_tasks(self):
        query = 'SELECT * FROM tasks'
        with DatabaseConnection(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        

    def fetch_task_by_id(self, id):
        query = f'SELECT * FROM tasks WHERE id = ? '
        with DatabaseConnection(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return cursor.fetchone()
        
    def delete_task(self, task_id):
        query = 'DELETE FROM tasks WHERE id = ?'
        with DatabaseConnection(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (task_id,))
            connection.commit()

    def update_task(self, task):
        query = """UPDATE tasks
        SET title = ?, description = ?, due_date = ?, priority = ?
        WHERE id = ? 
        """
        with DatabaseConnection(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query,(task.title, task.description, task.due_date, task.priority, task.id))
            connection.commit()
            



    
