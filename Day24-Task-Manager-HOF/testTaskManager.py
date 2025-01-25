import unittest
import taskManager
import os

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_tasks.json'
        taskManager.file_name = self.test_file
        with open(self.test_file, 'w') as f:
            f.write('[]')



    def test_create_task_file(self):

        # Add a task and verify it is added to the file
        taskManager.create_task_file('Clean Home', 'Medium', '1/1/2024', 'Completed')
        taskManager.create_task_file('Clean Home', 'Medium', '1/1/2024', 'Completed')

        tasks = taskManager.load_data()
        self.assertIn(
            {'task_name': 'Clean Home', 'priority': 'Medium', 'due_date': '1/1/2024', 'status': 'Completed'},
            tasks
        )
        

    def test_duplicate_tasks(self):
        # Check if duplicate tasks can be added in file
        taskManager.create_task_file('Clean Home', 'Medium', '1/1/2024', 'Completed')
        taskManager.create_task_file('Clean Home', 'Medium', '1/1/2024', 'Completed')

        tasks = taskManager.load_data()

        self.assertEqual(len(tasks), 1)


    def test_display_tasks(self):
        # Display all the tasks
        taskManager.create_task_file('Buy Groceries', 'High', '1/2/2024', 'Pending')
        taskManager.create_task_file('Submit Project', 'High', '1/2/2024', 'Completed')

        taskManager.display_tasks()

    def test_apply_to_tasks(self):
        # Test taht higher-order function can be applied to all tasks
        taskManager.create_task_file('Submit Project', 'High', '1/2/2024', 'Completed')

        taskManager.apply_to_tasks(taskManager.taged_tasks)
        tasks = taskManager.load_data()

        self.assertEqual(tasks[0].get('tag'), 'urgent')

    def test_filter_tasks(self):
        """Test that tasks can be filtered based on a condition."""
        taskManager.create_task_file('Buy Groceries', 'High', '1/2/2024', 'Pending')
        taskManager.create_task_file('Clean Home', 'Medium', '1/1/2024', 'Completed')

        high_priority_tasks = taskManager.filter_tasks(lambda task: task['priority'] == 'High')
        self.assertEqual(len(high_priority_tasks), 1)

    def test_summarize_tasks(self):
        """Test the summarization of tasks (pending vs completed)."""
        taskManager.create_task_file('Buy Groceries', 'High', '1/2/2024', 'Pending')
        taskManager.create_task_file('Clean Home', 'Medium', '1/1/2024', 'Completed')

        def summary_fun(pending, completed):
            return len(pending), len(completed)
        
        pending_count, completed_count = taskManager.summarize_tasks(summary_fun)
        
        self.assertEqual(pending_count, 1)
        self.assertEqual(completed_count, 1)

    def test_mark_as_completed(self):
        #Test marking a task as completed.
        taskManager.create_task_file('Buy Groceries', 'High', '1/2/2024', 'Pending')
        taskManager.change_status('Buy Groceries', 'Completed')
        tasks = taskManager.load_data()

        self.assertEqual(tasks[0]['status'], 'Completed')

    def test_delete_task(self): 
        # Test if task has been deleted successfully from file
        taskManager.create_task_file('Buy Groceries', 'High', '1/2/2024', 'Pending')
        taskManager.delete_task('Buy Groceries')
        tasks = taskManager.load_data()

        self.assertEqual(len(tasks), 0)


    def tearDown(self):
        # Delete the temporary test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()