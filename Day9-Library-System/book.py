from libraryItem import LibraryItem

class Book(LibraryItem):
  def __init__(self, title, author, publication_year, genre, status):
    super().__init__(title, author, publication_year, status)
    self.genre = genre
    