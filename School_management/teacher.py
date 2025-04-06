from person import Person

class Teacher(Person):
    def __init__(self, name, email, subject, assigned_class=None):

        super().__init__(name, email)
        self.subject = subject
        self.assigned_class = assigned_class

    def assign_class(self, class_name):
        self.assigned_class = class_name

    @property
    def to_dict(self):
        data = super().to_dict
        data.update({
            'subject': self.subject,
            'assigned_class': self.assigned_class

        })
        return data

