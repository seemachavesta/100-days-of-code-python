import unittest
from expense.expense_manager import ExpenseManager



class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        self.manager = ExpenseManager()
        self.manager.data = [
            ["2025-02-01", "Food", 10.5],
            ["2025-02-02", "Transport", 5.0],
            ["2025-02-03", "Food", 8.0],
        ]


    def test_expense_amount(self):
        self.assertEqual(self.manager.expense_amount(), [10.5, 5.0, 8.0])
        self.assertNotEqual(self.manager.expense_amount(), [3.9, 3.0, 0.0, -1.0])

    def test_total_expense(self):
        self.assertEqual(self.manager.total_expense(), 23.5)
        self.assertNotEqual(self.manager.total_expense(), 5.0)

    def test_average_expense(self):
        self.assertAlmostEqual(self.manager.average_expense(), 7.83, places= 2)


    def test_maximum_expense(self):
        self.assertEqual(self.manager.maximum_expense(), 10.5)

    def test_minimum_expnese(self):
        self.assertEqual(self.manager.minimum_expnese(), 5.0)

    def test_expenses_by_category(self):
        expected = {"Food": 18.5, "Transport": 5.0}
        self.assertEqual(self.manager.expenses_by_category(), expected)

    

# 
# python -m unittest discover -s test_expense_manager


if __name__ == "__main__":
    unittest.main()
