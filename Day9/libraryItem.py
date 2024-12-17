
class LibraryItem:
  def __init__(self, title, author, publication_year, status):
    self.title = title
    self.author = author
    self.publication_year = publication_year
    self.status = status
    
    
  def __repr__(self):
    return f"<{self.title}>"
    
  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Publication year: {self.publication_year}, Statu:  {self.status}"