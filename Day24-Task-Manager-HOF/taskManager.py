import json

file_name = 'tasks.json'

def load_data():
    """
    Loads task data from the JSON file.
    Returns:
        list: A list of task dictionaries. Returns an empty list if the file does not exist.
    """
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        

        
def create_task_file(task_name, priority, due_date, status):
    """Create a new task and save it to the JSON file if it doesn't already exist."""
    data = load_data()
    for task in data:
        if task_name == task['task_name']:
            print(f'Task {task_name} already exists in file. ')
            return 
        
    data.append(
        {'task_name': task_name,
          'priority': priority,
          'due_date': due_date,
          'status': status
        }
        )
        
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
        

def display_tasks():
    """Display all tasks in a formatted table with headers."""
    data = load_data() 
    
    # Print the header row with proper alignment
    print(f"{'Task':<20}{'Priority':<15}{'Due Date':<15}{'Status':<10}")
    print("-" * 40)  # Separator line for clarity

    # Print each task row
    for task in data:
        print(f"{task['task_name']:<20}{task['priority']:<15}{task['due_date']:<15}{task['status']:<10}")

        
def apply_to_tasks(func):
    """Apply a given function to each task and update the JSON file."""
    tasks = load_data()
    for task in tasks:
        func(task)
            
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)
        
    return tasks
    
    
def taged_tasks(task):
    """Tag tasks as 'urgent' if priority is 'High'; otherwise, tag as None."""
    if task['priority'] == 'High':
        task['tag'] = 'urgent'
    else:
        task['tag'] = None
        
        
def filter_tasks(predicate):
    """Filter tasks based on a given condition and return the filtered list."""
    tasks = load_data()
    return [task for task in tasks if predicate(task)]
    
        
def pending_tasks(task):
    #Check if the task status is pending and return task name and due date
    if task.get('status') == 'pending':
        print(f"{task['task_name']:<20}{task['due_date']:<15}")
        
        
def summarize_tasks(func):
    """Summarize pending and completed tasks by passing them to a summary function."""
    tasks = load_data()
    pending_tasks = [task for task in tasks if task['status'] == 'Pending']
    completed_tasks = [task for task in tasks if task['status'] == 'Completed']
    
    return func(pending_tasks, completed_tasks)
    
    
def task_summary(pending, completed):
    """Print the count of pending, completed, and total tasks."""
    total_tasks = len(pending) + len(completed)
    pending_task = len(pending)
    completed_task = len(completed)
    
    print(f"Pending Tasks: {pending_task}, Completed Task: {completed_task}, and Total Task: {total_tasks}")
        
   
        
def change_status(task_name, status):
    """Mark a task as completed or update its status."""
    tasks = load_data()
    task_index = {task['task_name']: i for i, task in enumerate(tasks)}
    
    if task_name in task_index:
        tasks[task_index[task_name]]['status'] = status
        print(f'Task status has been changed to {status}')
  
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

        
def delete_task(task_name):
    """Delete a task by its name and update the JSON file."""
    tasks = load_data()
    
    tasks = [task for task in tasks if task['task_name'] != task_name]
    print('Task has been deleted successfully.')
        
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)
        





