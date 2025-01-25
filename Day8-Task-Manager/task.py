class Task:
  def __init__(self, name, priority, due_date, status):
    self.name = name
    self.priority = priority
    self.due_date = due_date
    self.status = status
    
  def __repr__(self):
    return f'Task({self.name})'
    
  def __str__(self):
    return f"Name: {self.name}, Priority: {self.priority}, Due Date: {self.due_date}, Status:{self.status}"
  
  def mark_as_completed(self):
    
    if self.status == 'Completed':
      print('Task is already completed.')
    else:
      self.status = 'Completed'
      print(f'Task "{self.name}" marked as completed.')
      
    
  
  def update_task(self, name=None, priority=None, due_date=None, status=None):
    if name:
      self.name = name
      
    if priority:
      self.priority = priority
      
    if due_date:
      self.due_date = due_date
      
    if status:
      self.status = status
      
    print(f"Task updated: {self}")