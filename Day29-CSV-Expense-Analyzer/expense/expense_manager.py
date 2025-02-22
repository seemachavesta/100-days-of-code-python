import pandas as pd

class ExpenseManager:
    def __init__(self, file_name='expense.csv'):
        self.file_name = file_name
        self.header, self.data = self.load_data()
        
    def load_data(self):
        try:
            df = pd.read_csv(self.file_name)
            header, data = df.columns.tolist(), df.values.tolist()
            return header, data
        except FileNotFoundError:
            print(f"Error: {self.file_name} not found.")
            return [], []
            
    def expense_amount(self):
        return [float(amount[2]) for amount in self.data if isinstance(amount[2], (float, int))]
        
    def total_expense(self):
        amount = self.expense_amount()
        return sum(amount)
        
    def average_expense(self):
        expense = self.expense_amount()
        total = sum(expense)
        
        return total / len(expense) if expense else 0.0
        
    def maximum_expense(self):
        expense = self.expense_amount()
        return max(expense) if expense else 0
        
    def minimum_expnese(self):
        expense = self.expense_amount()
        return min(expense) if expense else 0
        
        
    def expenses_by_category(self):
        category_summary = {}
    
        for expense in self.data:
            category, amount = expense[1],  expense[2]
            category_summary.setdefault(category, 0)
            category_summary[category] +=  amount
        
        return category_summary
        
    def save_summary(self):
        expnese_summary = self.expenses_by_category()
        df = pd.DataFrame(list(expnese_summary.items()), columns=['Category', 'Amount'])
        df.to_csv('expense_summary.csv', index=False)