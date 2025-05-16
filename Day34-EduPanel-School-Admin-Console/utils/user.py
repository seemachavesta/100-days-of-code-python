class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __repr__(self):
        return f'Username: {self.username}, Role: {self.role}'