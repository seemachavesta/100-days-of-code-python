class Book:
  def __init__(self, title, author, status):
    self.title = title
    self.author = author
    self.status = status
    
class Library:
  def __init__(self):
    self.name = "City Library"
    self.location = "Down Town"
    self.books = {}
    
   # checking the book title  if available in books
  def check_for_title(self, title):
    if title in self.books:
      return True
    else:
      print(f"The book '{title}' is not available.")
      return False
      
   #adding the book in library  
  def add_book(self, book):
    if book.title in self.books:
      print(f"The book '{book.title}' already exists in the library.")
      return
    
    self.books[book.title] = book
    print(f"Book '{book.title}' by {book.author} added to the library.")
    
#Displaying the list of books
  def list_books(self):
    for title, book in self.books.items():
      print(f"'{title}' by {book.author} - Status: {book.status}")
  
  #Removing the book from books
  def remove_book(self, title):
    if not self.check_for_title(title):
      return 
    
    del self.books[title]
    print(f"Book '{title}' removed from the library.")
    
  
  def lend_book(self, title):
    if not self.check_for_title(title):
      return 
   
    book = self.books[title]
    if book.status == 'Available':
      book.status = 'Borrowed'
      print(f"Book '{title}' has been borrowed.")
    else:
      print(f"Book '{title}' has already been borrowed.")
    
      
  def return_book(self, title):
    if not self.check_for_title(title):
      return 
    book = self.books[title]
    if book.status == 'Borrowed':
      book.status = 'Available'
      print(f"The '{title}' has been returned.")
    else:
      print(f"Book '{title}' was not borrowed.")
    
    
      

library = Library()
      
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Available")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Available")
book3 = Book("1984", "George Orwell", "Available")
book4 = Book("Learning Python", "Mark Lutz", "Available")

# adding books in library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

#user menu to choose
menu_prompt = "\nEnter 'l' to view list of books, 'b' to borrow, 'r' to return, 'q' to quit:  "

print('Welcome in Library Management System')

while True: 
  
  user_choice = input(menu_prompt).lower()
  
  if user_choice == 'l':
    library.list_books()
    
  elif user_choice == 'b':
    user_input = input('Enter the book title you want to borrow: ')
    library.lend_book(user_input)
    
  elif user_choice == 'r':
    user_input = input("Enter the book title you want to return: ")
    library.return_book(user_input)
    
  elif user_choice == 'q':
    break
  
  else:
    print('Invlid choice.')