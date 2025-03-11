class Task:
    def __init__(self, id, title, description, due_date, priority):
         self.id = id
         self.title =  title
         self.description = description
         self.due_date = due_date 
         self.priority = priority


    def to_dict(self):
         return {
              'id': self.id,
              'title': self.title,
              'description': self.description,
              'due_date': self.due_date,
              'priority': self.priority
         }
        