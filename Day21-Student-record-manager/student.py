class Student:
    # Represents a student with an ID, name, and a list of subjects with grades.
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.subjects = []
        
    def __repr__(self):
        # Return a string representation of the student object
        return f'Id: {self.id}, name: {self.name} subjects and grades: {self.subjects}'
        
    def to_dict(self):
        # Converts the student object into a dictionary format for easy JSON serialization
        return {'id': self.id, 'name': self.name, 'subjects': self.subjects}
        
    def add_subject(self, subject, grade):
        # Adds a subject and its grade to the student's record
        self.subjects.append({'subject': subject, 'grade': grade})