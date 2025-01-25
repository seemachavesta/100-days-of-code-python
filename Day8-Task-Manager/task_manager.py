from task import Task
class TaskManager:
  def __init__(self):
    self.tasks = {}
    
    
  def __len__(self):
    return len(self.tasks)
    
  def _filter_tasks(self, attribute, value):
    return [task for task in self.tasks.values() if getattr(task, attribute) == value]
    
# add_task(task) to add a task to the task list.
  def add_task(self, task):
    if task.name in self.tasks:
      print(f'{task} already exist.')
      return
    
    self.tasks[task.name] = task
    print(f'Task {task} has beena added successfully!')
    
    
    
# remove_task(task_name) to remove a task by its name.
  def remove_task(self, name):
    if name in self.tasks:
      del self.tasks[name]
      print(f"Task '{name}' has been removed.")
    else:
      print(f"Task {name} is not found.")
  
# view_all_tasks() to display all tasks.
  def view_all_tasks(self):
    if len(self.tasks) >= 0:
      print('There are no task to view')
      
    for task in self.tasks.values():
      print(task)
      print(f'-'*30)
    
      
# view_pending_tasks() to show only pending tasks.
  def view_pending_tasks(self):
    pending_tasks = self._filter_tasks('status', 'Pending')
    
    if pending_tasks:
      for task in pending_tasks:
        print(task)
        print('-'*30)
   
          
# view_completed_tasks() to show completed tasks.
  def view_completed_tasks(self):
    completed_tasks = self._filter_tasks('status', 'Completed')
    if completed_tasks:
      for task in completed_tasks:
        print(task)
        print('-'*20)
          

    
        
# search_by_priority(priority) to find tasks by priority.
  def search_by_priority(self, priority):
    task_by_priority = self._filter_tasks('priority', priority)
    if task_by_priority:
      for task in task_by_priority:
        print(task)
        print('-'*30)
    else:
      print(f'Task with priority of {priority} is not found.')
      
# search_by_due_date(date) to find tasks by due date.
  def search_by_due_date(slef, date):
    due_date = self._filter_tasks('due_date', date)
    if due_date:
      for task in due_date:
        print(task)
    else:
      print(f'Task with due date of {date} not found')



