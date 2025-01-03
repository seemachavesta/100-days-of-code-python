import sqlite3

# DatabaseManager class handles all database operations
class DatabaseManager:
    # Initialize the database manager with the database name
    def __init__(self, db_name = 'contacts.db'):
        self.db_name = db_name

   # Create contacts table in database
    def create_table(self):
        # Create the contacts table if it doesn't already exist
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT, number TEXT PRIMARY KEY, email TEXT)')
            connection.commit()
    
    #Insert contact in table
    def insert_contact(self, contact):
        # Insert or replace a contact in the contacts table
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''INSERT OR REPLACE INTO contacts (name, number, email)
                           VALUES (?, ?, ?)''', (contact.name, contact.number, contact.email))
            
            connection.commit()
            
    def fatch_contact(self):
        # Fetch and display all contacts from the contacts table
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM contacts')
            
            contacts = cursor.fetchall()
        
        for contact in contacts:
            name, number, email = contact
            print(f'Name: {name}\nNumber: {number}\nEmail: {email}')
            print('-' * 30)

    def delete_contact(self, name):
        # Delete a contact by name from the contacts table
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))

        # Check if a contact was deleted
        if cursor.rowcount == 0:
            print(f"No contact found with the name '{name}'.")
        else:
            print(f"Contact with the name '{name}' deleted successfully.")

        connection.commit()
        
       

