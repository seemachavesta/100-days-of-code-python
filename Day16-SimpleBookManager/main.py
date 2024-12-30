import book_functions

# Menu for user interaction
user_menu = """ 
Enter

- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete book
- 'q' to quit

your choice: """

# Main program loop
def main():
    while True:
        user_input = input(user_menu).strip().lower()
        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            book_functions.list_books()

        elif user_input == 'r':
            prompt_read_book()

        elif user_input == 'd':
            prompt_delete_book()

        elif user_input == 'q':
            break
        else:
            print('Enter a valid choice: ')



# Function to prompt the user for book details and add the book
def prompt_add_book():
    book_name = input('Enter the book name: ').title()
    author_name = input('Enter the author name: ').title()
    book_functions.add_book(book_name, author_name)

# Function to prompt the user for book details and mark the book as read
def prompt_read_book():
    book_name = input('Enter the book name: ').title()
    author_name = input('Enter the author name: ').title()

    book_functions.mark_book_as_read(book_name, author_name)

# Function to prompt the user for book details and delete the book
def prompt_delete_book():
    book_name = input('Enter the book name: ').title()
    author_name = input('Enter the author name: ').title()

    book_functions.delete_book(book_name, author_name)


# Start the program
if __name__ == '__main__':
    main()


