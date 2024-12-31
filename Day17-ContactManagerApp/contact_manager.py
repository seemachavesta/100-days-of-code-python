import csv

class ContactManager:
    def __init__(self, file_name='contacts.csv'):
        self.file_name = file_name
        
   
    #Create CSV file if it doesn't exist
    def create_file(self):
        with open(self.file_name, 'w', newline='') as file:
            pass

    #Load contact data from CSV file, create file if not foun   
    def load_file(self):
        try:
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                existing_contact = [contact for contact in reader]
                return existing_contact
                
        except FileNotFoundError:
            self.create_file()
            return []
            
    #Add new contact and check for duplicates
    def add_contact(self, contact):
        existing_contacts = self.load_file()
        # creating a new list with current information 
        contact_data = [contact.name, contact.phone, contact.email]
        
        # Check for duplicates before adding a new contact
        if contact_data in existing_contacts:
            print(f'{contact.name} already exists in contacts')
            return
            
        
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(contact_data)
            
    # List all contacts from CSV file
    def view_contacts(self):
        # Logic to read and display all contacts
        contacts = self.load_file()
        
        if not contacts:
            print('There is no contact available')
            return
        
        print('All Contacts:')
        print('-' * 30)
        for contact in contacts:
            name, phone, email = contact
            print(f'Name: {name}\nPhone Number: {phone}\nEmail: {email}')
            print('-' * 30)
    
    # Search for contact by name
    def search_contact(self, name):
        contacts = self.load_file()
        
        for contact in contacts:
            contact_name, phone, email = contact
            if contact_name == name:
                print(f'Name: {contact_name}, Phone: {phone}, Email: {email}')
                return
        else:
            print('Contact not found')

    # Delete contact by name
    def delete_contact(self, name):
        # Logic to delete a contact by name
        contacts = self.load_file()
        
        updated_contacts = [contact for contact in contacts if name not in contact]

        
        with open(self.file_name, 'w', newline= '') as file:
            writer = csv.writer(file)
            writer.writerows(updated_contacts) 
        
        print(f'Contact {name} has been deleted successfully.')