from task import Task
from task_manager import TaskManager


task_manager = TaskManager()

task1 = Task('Shopping', 'Low', '12-1-2024', 'Pending')
task2 = Task('Studying', 'High', '12-2-2024', 'Completed')
task3 = Task('Cleaning', 'Medium', '12-1-2024', 'Pending')

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

menu_prompt = """
Task Manager Menu:
-------------------
Enter:
'a' to Add a new task
'l' to View all tasks
'v' to View pending tasks
'c' to View completed tasks
'p' to Search tasks by priority
'd' to Search tasks by due date
'u' to Update an existing task
'r' to Remove a task
'q' to Quit

What would you like to do? 
"""
# Asking user to provide input for action to persom
while True:
  user_input = input(menu_prompt).lower()
  if user_input == 'a':
    try:
      new_task = input('Enter the task by name, priority, due date, and status (comma-separated): ')

      name, priority, due_date, status = map(str.strip, new_task.split(',') )
      
      task = Task(name, priority, due_date, status)
      task_manager.add_task(task)
    except ValueError:
      print('Invalid input format')
    
  elif user_input == 'l':
    task_manager.view_all_tasks()
    
  elif user_input == 'v':
    task_manager.view_pending_tasks()
    
  elif user_input == 'c':
     task_manager.view_completed_tasks()
     
  elif user_input == 'p':
    priority = input('Enter the priority date: ')
    task_manager.search_by_priority(priority)
    
  elif user_input == 'd':
    date = input('Enter the due date: ')
    task_manager.search_by_due_date(date)
    
  elif user_input == 'u':
    name = input('Enter the task name to update: ')
    if name in task_manager.tasks:
        task = task_manager.tasks[name]
        new_name = input('Enter new name (or leave blank): ').strip()
        new_priority = input('Enter new priority (or leave blank): ').strip()
        new_due_date = input('Enter new due date (or leave blank): ').strip()
        new_status = input('Enter new status (or leave blank): ').strip()
        task.update_task(
            name=new_name or None,
            priority=new_priority or None,
            due_date=new_due_date or None,
            status=new_status or None
        )
    else:
        print(f"Task '{name}' not found.")
  
  elif user_input == 'r':
    name = input('Enter the task name you want to remove: ')
    task_manager.remove_task(name)
  
  elif user_input == 'q':
    print('Goodbye!')
    break
  else:
    print('Invlid Choice')
  
    
    