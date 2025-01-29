class Article:
    def __init__(self, title: str, url: str, category: str, date: str):
        self.title = title
        self.url = url
        self.category = category
        self.date = date
        self.read = 0

    def __repr__(self):
        return f"Title: {self.title}, url: {self.url}, Category: {self.category}, Date: {self.date}"