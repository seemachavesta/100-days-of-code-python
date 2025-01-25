from libraryItem import LibraryItem
from magazine import Magazine
from book import Book
from libraryMember import LibraryMember

class Library:
  def __init__(self):
    self.items = {}
    
    
  def add_item(self, item, force=False):
    if not isinstance(item, LibraryItem):
      print("Invalid item. Only LibraryItem objects can be added.")
      return 
      
    if item.title in self.items and not force:
      print(f'{item.title} already exists')
      return
      
    self.items[item.title] = item
          
   # Dsiplay the books and magzines   
  def display_items(self):
    for  item in self.items.values():
      if isinstance(item, Book):
        print(f"Book - Title: {item.title}, Author: {item.author}, Year: {item.publication_year}, Genre: {item.genre}, Status: {item.status}")
      elif isinstance(item, Magazine):
        print(f"Magazine - Title: {item.title}, Author: {item.author}, Year: {item.publication_year}, Issue: {item.issue_number}, Status: {item.status}")
      else:
        print(f"Library Item - Title: {item.title}, Author: {item.author}, Year: {item.publication_year}, Status: {item.status}")

  # Allow user to borrow item from library      
  def lend_item(self, item_title):
    
    if item_title not in self.items:
      print(f"{item_title} is not available in the library.")
      return None

    item = self.items[item_title]
    if item.status != 'Available':
      print(f"{item.title} is currently not available.")
      return None

    item.status = 'Borrowed'
    return item


  def return_item(self, item):
    if item.title in self.items:
      self.items[item.title].status = 'Available'
    else:
      self.items[item.title] = item 
      print(f"{item.title} has been returned to the library.")



book1 = Book('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction', 'Available')
book2 = Book('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 'Available')
magazine1 = Magazine('National Geographic', 'Various Contributors', 2023, 150, 'Available')
magazine2 = Magazine('Person of the Year', 'Various Contributors', 2022, 48, 'Available')

library = Library()
# Add the Book and Magazine objects directly to the library
library.add_item(book1)
library.add_item(book2)
library.add_item(magazine1)
library.add_item(magazine2)


# library.display_items()


member = LibraryMember("Alice", 1)

member.borrow_item(library, "The Hobbit")
member.borrow_item(library, "National Geographic")
member.borrow_item(library, 'Person of the Year')

library.display_items()

member.return_book(library, 'Person of the Year')
member.return_book(library, 'National Geographic')
library.display_items()