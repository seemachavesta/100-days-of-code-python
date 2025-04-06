class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


    def update_email(self, new_email):
        self.email = new_email

    @property
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email

        }