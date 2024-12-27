class Expense:
    def __init__(self, category, description, amount, date):
        self.category = category
        self.description = description
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f'Category: {self.category}, Description: {self.description}, Amount: {self.amount}, Date: {self.date}'

    def to_string(self):
        return f'{self.category}, {self.description}, {self.amount}, {self.date}'


