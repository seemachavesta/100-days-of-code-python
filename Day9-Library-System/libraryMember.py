class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = {}

    def borrow_item(self, library, item_title):
      if item_title in self.borrowed_items:
        print(f"{item} is already borrowed by {self.name}.")
        return
        
      item = library.lend_item(item_title)
      if item:
        self.borrowed_items[item.title] = item
        print(f"{self.name} borrowed {item.title}.")

    def return_book(self, library, book_title,):
       if book_title not in self.borrowed_items:
          print(f"{book_title} was not borrowed by {self.name}.")
          return 
       
       book = self.borrowed_items.pop(book_title)
       library.return_item(book)
       print(f"{self.name} returned {book.title}.")
          

        
       
            


    






