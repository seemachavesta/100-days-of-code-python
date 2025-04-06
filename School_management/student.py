from person import  Person
class Student(Person):
    def __init__(self, name, email, grade, enrolled_class=None):
        super().__init__(name, email)
        self.grade = grade
        self.enrolled_class = enrolled_class

    def update_grade(self, new_grade):
        self.grade = new_grade

    def enroll_in_class(self, class_name):
        self.enrolled_class = class_name

    @property
    def to_dict(self):
        data = super().to_dict
        data.update({
            'grade': self.grade,
            'enrolled_class': self.enrolled_class
        })
        return data

