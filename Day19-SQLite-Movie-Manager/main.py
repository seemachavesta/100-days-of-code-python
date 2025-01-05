from utils import database


# Menu-driven application to interact with the movie database.
user_menu = '''Enter
- 'a' to add a movie
- 'l' to list movies
- 's' to search for a movie by name
- 'd' to delete a movie from the collection
- 'q' to quit
Your choice: '''

# Ensure the table exists before any operation.
def setup_database():
    database.create_table()



# Prompt the user to add a new movie to the database
def prompt_add_movie():
    try:
        title = input('Enter movie title: ').strip()
        genre = input('Enter movie genre: ').strip()
        year = int(input('Enter movie release year: '))
        rating = float(input('Enter movie rating: '))
        database.insert_movie(title, genre, year, rating)
    except ValueError:
        print("Invalid input. Please enter correct data types.")

# Prompt the user to search for a movie by its title.
def prompt_search_movie():
    title = input('Enter movie title: ').strip()
    database.search_movie(title)

# Prompt the user to delete a movie from the database by its title.
def prompt_delete_movie():
    title = input('Enter movie title: ')
    database.delete_movie(title)

# Print all movies list
def display_movies():
    movies = database.get_all_movies()
    print(f"{'ID':<5} {'Title':<30} {'Genre':<20} {'Release Year':<15} {'Rating':<10}")
    print('-' * 80)  

    for movie in movies:
        id, title, genre, year, rating = movie
        print(f"{id:<5} {title:<30} {genre:<20} {year:<15} {rating:<10}")
        print()





def main():
    # Main loop to display the user menu and handle user input.
    while True:
        setup_database()
        choice = input(user_menu).lower()
        if choice == 'a':
            prompt_add_movie()
        elif choice == 'l':
            display_movies()
        elif choice == 's':
            prompt_search_movie()
        elif choice == 'd':
            prompt_delete_movie()
        elif choice == 'q':
            break
        else:
            print('Invalid Choice, Try again')



if __name__ == '__main__':
    main()