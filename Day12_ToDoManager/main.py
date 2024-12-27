class Task:
    def __init__(self,task_name, due_date, status):
        self.task_name = task_name
        self.due_date = due_date
        self.status = status
        
    def __repr__(self):
        return f'<Task: {self.task_name}, Due Date: {self.due_date}, Status: {self.status}>'
     
 
        
class ToDoManager:
    task_list = {}
    
    #Helper function to check task status
    @classmethod 
    def check_task_status(cls, task_name):
        return task_name in cls.task_list
    
    # Add tasks in task list
    @classmethod
    def add_task(cls, task):
        if task.task_name in cls.task_list:
            print(f'Task {task.task_name} already exists.')
            return
    
        cls.task_list[task.task_name] = task

     #Remove task from task list when task name is provided   
    @classmethod
    def remove_task(cls, task_name):
        if cls.check_task_status(task_name):
            del cls.task_list[task_name]
            print(f'Task {task_name} has been removed.')
            return
        
        print(f'Task {task_name} does not exist')
           
            
        
     #Display the total count of tasks   
    @classmethod
    def total_tasks(cls):
        length = len(cls.task_list)
        task_word = "Task" if length == 1 else "Tasks"
        return f'There are {length} {task_word} in the list.'

        
    @classmethod
    def display_tasks(cls):
        if not cls.display_tasks:
            print("No tasks to display.")
            return
        
        for task in cls.task_list.values():
            print(task)
    
    #This function change the task status     
    @classmethod
    def change_status(cls, task_name, new_status):
       #If task name exists in task list
       if cls.check_task_status(task_name):
           # Assign new task status to old status
           cls.task_list[task_name].status = new_status
           return
       
       print(f'Task {task_name} does not exist')
           
        
        
        
             
# Test cases
task1 = Task('Shopping', 'Tomorrow', 'Pending')
task2 = Task('Reading', 'Tomorrow', 'Pending')

ToDoManager.add_task(task1)
ToDoManager.add_task(task2)

ToDoManager.display_tasks()
print(ToDoManager.total_tasks())

ToDoManager.change_status('Shopping', 'Completed')
ToDoManager.display_tasks()

ToDoManager.remove_task('Shopping')
ToDoManager.display_tasks()