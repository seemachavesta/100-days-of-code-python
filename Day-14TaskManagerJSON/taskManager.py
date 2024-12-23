import json
from task import Task

        
class TaskManager:
    #Load task  during initialization
    def __init__(self):
        try:
            with open('task.json', 'r') as task_file:
                self.task_list = json.load(task_file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.task_list = {}
        
        
    # Add task in json file   
    def add_task_in_file(self):
        try:  
            with open('task.json', 'w') as file:
                json.dump(self.task_list, file, indent=4)
        except IOError as e:
            print(f'Error writing to file: {e}') 
            
     # Add task in task list using the  task name as key   
    def add_task(self, task):
       #check if task already exist in task list
        if task.task_name in self.task_list:
            print(f'Task {task.task_name} already exist.')
            return
        self.task_list[task.task_name] = task.to_dict()
        
        self.add_task_in_file()
            
        print(f'Task {task.task_name}  has been added')
        
    # display all task   
    def display_tasks(self):
        # check if task list in not empty
        if not self.task_list:
            print('No task to display.')
            return
        #Looping over the the task list to print out each task
        for name, task in self.task_list.items():
            print(f"Task Name: {name}, Status: {task['status']}, Due Date: {task['due']}")
            print("-" * 35)
            
    # Removing task from task list and adding new task list in json file
    def remove_task(self, task):
        
        if task.task_name not in self.task_list:
            print(f'Task {task.task_name} not in task list.')
            return
        #delete the task from tasklist using task name
        del self.task_list[task.task_name]
        #function to add updated tasklist in json file
        self.add_task_in_file()
        
        print(f'Task {task.task_name} has been deleted successfully.')
        
        
        
        
task_manager = TaskManager()       
 

task1 = Task("Study", "Pending", "Tomorrow")
task2 = Task('Shopping', 'Completed', 'Today')
task3 = Task('Cleaning', 'Completed', 'Yesterday')


task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.remove_task(task1)

task_manager.display_tasks()
  
