from bs4 import BeautifulSoup

from locators.all_book_page import AllBooksPage
from parsers.book_parser import BookParser


class BookPage:
    def __init__(self, page):
        self.page = page 
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = AllBooksPage.BOOK
        
        book_link = self.soup.select(locator)
        book = [BookParser(e) for e in book_link]
        return book