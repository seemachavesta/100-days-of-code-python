class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

    def to_string(self):
        return f"{self.name},{self.phone},{self.email}"