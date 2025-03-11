
from utils.task import Task

from utils.linkedList import LinkedList
from utils.logger import Logger
from utils.database import Database




class TaskManager:
    def __init__(self):
        # Set up the database and logger, and initialize the LinkedList
        self.db = Database()
        self.db.create_table()
        self.linkedList = LinkedList()
        Logger.setup_logger()
        
        
    def add_task(self, task):
        # Add a new task if the task ID does not already exist
        tasks = self.db.fetch_all_tasks()
        existing_task_ids = {t[0] for t in tasks}
        if task.id not in existing_task_ids:
            self.db.insert_task(task)
            Logger.log_task_added(task)
        else:
            print(f"Task with ID {task.id} already exists.")

    def update_task(self, id):
        task = self.db.fetch_task_by_id(1)
        if task:
            print("Enter new details:")
            new_title = input("New title: ")
            new_description = input("New description: ")
            new_due_date = input("New due date: ")
            new_priority = input("New priority: ")
            self.db.update_task(id, new_title, new_description, new_due_date, new_priority)
            updated_task = Task(id, new_title, new_description, new_due_date, new_priority)
            Logger.log_task_updated(updated_task)
        else:
            print(f'No task found with id {id}')


    def mark_task_completed(self, id):
        # Mark a task as completed and add it to the LinkedList
        task = self.db.fetch_task_by_id(id)
        if task:
            completed_task = Task(*task)
            self.linkedList.insert_at_beginning(completed_task)
            Logger.log_task_completed(task)

    def get_all_tasks(self):
        # Display all tasks stored in the database
        tasks =  self.db.fetch_all_tasks()

        if not tasks:
            print('There is no task to display')
            return 
        
        print("\nAll Tasks:")
        print("-" * 50)
        for task in tasks:
            task_id, title, description, due_date, priority = task
            print(f"ID: {task_id}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nPriority: {priority}")
            print("-" * 50)

    def get_recently_completed(self):
        # Show recently completed tasks using LinkedList
        self.linkedList.print_recently_completed()

    def delete_task(self, id):
        # Delete a task by ID from the database
        self.db.delete_task(id)
        Logger.log_task_deleted(id)

    


        
        








        