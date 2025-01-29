from .databaseConnection import DatabaseConnection

class ArticleManager:
    def __init__(self, file_name="data.db"):
        self.file_name = file_name

    
    def create_table(self):
        # Create articles table in the database
        query = """
        CREATE TABLE IF NOT EXISTS articles (
        title TEXT PRIMARY KEY,
        url TEXT,
        category TEXT,
        date TEXT,
        read INTEGER);"""

        with DatabaseConnection(self.file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

    # Add an article to the database using the Article class
    def add_article(self, article):
        query = 'SELECT COUNT(*) FROM articles WHERE title = ?'
        insert_query = 'INSERT INTO articles VALUES(?, ?, ?, ?, ?)'

        with DatabaseConnection(self.file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (article.title,))
            result = cursor.fetchone()
            if result[0] == 0:
                cursor.execute(insert_query, (article.title, article.url, article.category, article.date, article.read))
                connection.commit()

     # Display all articles in the database
    def display_articles(self):
        select_query = 'SELECT * FROM articles'

        with DatabaseConnection(self.file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(select_query)
            return cursor.fetchall()
         


     # Filter articles using a custom function
    def filter_article(self, func, criteria, value ):
        if criteria not in ["title", "category", "read"]:
            raise ValueError("Invalid criteria provided")

        query = f"SELECT * FROM articles WHERE {criteria} = ?"
        return func(query, value)
    
    
    # Display the summary of filtered articles
    def filter_summary(self, query, value):
        with DatabaseConnection(self.file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (value,))

            articles = cursor.fetchall()
            
            for article in articles:
                title, url, category, date, read = article
                read_status = 'No' if read == 0 else 'Yes'
                print(f"Title {title}, URL: {url}, Category: {category}, Date: {date}, Read: {read_status}")
            

    
     # Change the read status of an article by title
    def change_read_status(self, title, status):
        select_query = "SELECT * FROM articles WHERE title = ?"
        update_query = "UPDATE articles SET read = ? WHERE title = ?"

        with DatabaseConnection(self.file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(select_query, (title,))
            article = cursor.fetchall()
            if article:
                cursor.execute(update_query, (status, title))
                connection.commit()
                print(f"Read status for '{title}' updated to {status}.")
            else:
                print(f"Article with title '{title}' not found.")

    # Delete an article by title
    def delete_article(self, title):
        select_query = "SELECT * FROM articles WHERE title = ?"
        delete_query = "DELETE FROM articles WHERE title = ?"

        with DatabaseConnection(self.file_name) as connection:
            cursor = connection.cursor()
            cursor.execute(select_query, (title,))
            article = cursor.fetchone()
            if article:
                cursor.execute(delete_query, (title,))
                connection.commit()
                print(f"Article with title {title} has been deleted successfully.")
            else:
                print(f"Article with title '{title}' not found.")

                      
        
                        
            

    













