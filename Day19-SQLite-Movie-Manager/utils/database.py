from .database_connection import DatabaseConnection
from typing import List

# Create the 'movies' table if it doesn't already exist.
def create_table() -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                          (movie_id INTEGER PRIMARY KEY, 
                           title TEXT, 
                           genre TEXT,
                           release_year INTEGER,
                           rating REAL)''')


# Insert a new movie into the database if it doesn't already exist.
def insert_movie(title: str, genre: str, year: int, rating: float) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        
         # Check if the movie already exists to avoid duplicates.
        cursor.execute('''SELECT * FROM movies WHERE title = ?''', (title,))
        existing_movie = cursor.fetchone()
        
        if existing_movie:
            print(f"The movie '{title}' already exists in the database.")
        else:
            # Add the movie to the database if it doesn't exist.
            cursor.execute('''INSERT INTO movies 
                              (title, genre, release_year, rating)
                              VALUES (?, ?, ?, ?)''', 
                              (title, genre, year, rating))
            print(f"Movie '{title}' has been added to the database.")


# Retrieve and return movies list from the database.
def get_all_movies() -> List:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM movies')
        return cursor.fetchall()
    

 # Search for a specific movie by its title.       
def search_movie(title:str) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM movies WHERE title = ?', (title,))
        movie = cursor.fetchone()

        if not movie:
            print(f'Movie {title} was not found')
            return

        id, title, genre, year, rating = movie
        print(f"{id:<5} {title:<30} {genre:<20} {year:<15} {rating:<10}")
        print()
            


# Delete a movie from the database by its title.
def delete_movie(title: str) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM movies WHERE title = ?', (title,))
        print(f'Movie "{title}" was deleted successfully.')