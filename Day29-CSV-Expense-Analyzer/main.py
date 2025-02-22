from expense.expense_manager import ExpenseManager
      
def main():
    expense_manager = ExpenseManager()
    
    expense_manager.save_summary()
    
    # Print Total Expenses
    print("Total Expense:", expense_manager.total_expense())
    
    # Print Average Expense
    print("Average Expense:", expense_manager.average_expense())
    
    # Print Maximum Expense
    print("Maximum Expense:", expense_manager.maximum_expense())
    
    #print Minimum Expense
    print("Minimum Expense:", expense_manager.minimum_expnese())
    
    # Print Expenses by Category
    print("Expenses by Category:", expense_manager.expenses_by_category())
    
    
    
    
if __name__ == "__main__":
    main()