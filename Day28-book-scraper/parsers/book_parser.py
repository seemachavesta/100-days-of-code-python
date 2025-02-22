
from locators.book_locators import BookLocators



class BookParser:

    RATING = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent


    def __repr__(self):
        return f"Book: {self.name}, Price: {self.price}, Link: {self.link}, Rating: {self.rating}"
    

    @property
    def name(self): 
        locator = BookLocators.NAME
        item_link =  self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name
    
    @property
    def price(self):
        lacator = BookLocators.PRICE
        item_price =  self.parent.select_one(lacator).string

        return float(item_price.replace("£", ""))


    @property
    def link(self):
        lactor = BookLocators.LINK
        return self.parent.select_one(lactor).attrs['href']
    
    @property
    def rating(self):
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
    
        if star_rating_tag is None:
            return "No Rating"  # Handle missing ratings gracefully
    
        classes = star_rating_tag.attrs.get('class', []) 
        rating_classes = [r for r in classes if r != 'star-rating']
        rating = BookParser.RATING.get(rating_classes[0], 'No Rating')
        return rating