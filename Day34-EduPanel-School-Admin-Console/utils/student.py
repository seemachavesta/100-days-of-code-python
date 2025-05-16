class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}, Grade: {self.grade} "

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'grade': self.grade
        }