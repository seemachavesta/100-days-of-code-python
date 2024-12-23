class Task:
    def __init__(self, task_name, status, due_date):
        self.task_name = task_name
        self.status = status
        self.due_date = due_date
        
        
    def __repr__(self):
        return f'Task: {self.task_name}, Status: {self.status}, Due: {self.due_date}'
        
    def to_dict(self):
        return {"status": self.status, "due": self.due_date}
        