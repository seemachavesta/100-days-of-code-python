
class Employee:
    def __init__(self, id, name, designation):
        self.id = id
        self.name = name
        self.designation = designation

class Manager(Employee):
    def __init__(self, id, name, designation, team_size):
        super().__init__(id, name, designation)
        self.team_size = team_size

    def __repr__(self):
        return f'Employee id: {self.id}, Name: {self.name}, Designiation: {self.designation}, Team Size: {self.team_size}'
    

class Developer(Employee):
    def __init__(self,id, name, designation, programming_language):
        super().__init__(id, name, designation)
        self.programming_language = programming_language

    def __repr__(self):
        return f'Employee id: {self.id}, Name: {self.name}, Designiation: {self.designation}, Programming Lanaguage: {self.programming_language}'


class Intern(Employee):
    def __init__(self, id, name, designation, duration):
        super().__init__(id, name, designation)
        self.duration = duration

    def __repr__(self):
        return f'Employee id: {self.id}, Name: {self.name}, Designiation: {self.designation}, Duration: {self.duration}'