from libraryItem import LibraryItem  
    
class Magazine(LibraryItem):
  def __init__(self, title, author, publication_year, issue_number, status):
    super().__init__(title, author, publication_year,status)
    self.issue_number = issue_number