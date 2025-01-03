from databaseManager import DatabaseManager

# Contacts class represents an individual contact
class Contacts:
     # Initialize a contact with name, number, and email
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def __repr__(self):
         # String representation of the contact
        return f'Name {self.name}, Number: {self.number}, Email: {self.email}'
    

# Example usage
contact1 = Contacts('Farah', '333-222-9999', 'farah@test.com')
contact2 = Contacts('Emily', '444-232-1800', 'emily@test.com')

  # Initialize the database manager
db_manager = DatabaseManager()
db_manager.create_table()

#Insert contacts
db_manager.insert_contact(contact1)
db_manager.insert_contact(contact2)

#Display contacts
db_manager.fatch_contact()

#Delete contacts
db_manager.delete_contact('Farah')

# Fetch and display all remaining contacts
db_manager.fatch_contact()