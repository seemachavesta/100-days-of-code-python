import json

# Name of the JSON file used for storing book data
file_name = 'books.json'

# Function to read the JSON file and return the list of books
def read_file():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print('File not found')
        return []
    
# Function to write the list of books to the JSON file   
def write_in_file(books):
    with open(file_name, 'w') as file:
        json.dump(books, file, indent=4)
        
# Function to add a new book         
def add_book(name, author):
    # read the current books file
    books = read_file()
     
    # Check for duplicate books before adding
    for book in books:
        if name == book['name'] and author == book['author']:
            print(f"The book '{name}' by '{author}' already exists.")
            print('-' * 30)
            return
    # Add the new book in list   
    books.append({'name': name, 'author': author, 'read': False})
    #Add the books list in json file
    write_in_file(books)

# Function to list all books      
def list_books():
    books = read_file()

    #check if book list is empty 
    if not books:
        print("The list of books is empty.")
        return
    
    # Iterate over the books and display details
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"Book: {book['name']}, Author: {book['author']}, Read: {read}")
        print('-'* 30)

# Function to mark a book as read
def mark_book_as_read(name, author):
    books = read_file()

    # Flag to check if the book was found
    book_found = False

    for  book in books:
        if book['name'] == name and book['author'] == author:
            book['read'] = True
            book_found = True

    if not book_found:
        print(f"The book '{name}' by '{author}' was not found.")
        return
    
    write_in_file(books)



# Function to delete a book
def delete_book(name, author):
    books = read_file()
    
    # Check if the book exists before trying to delete
    book_found = any(book['name'] == name and book['author'] == author for book in books)
    if not book_found:
        print(f"The book '{name}' by '{author}' was not found.")
        return
    
   # Remove the book from the list
    books = [book for book in books if not (name == book['name'] and author == book['author'])]
    
    # Save the updated list back to the file
    write_in_file(books)
    
    print(f"The book '{name}' by '{author}' has been deleted.")