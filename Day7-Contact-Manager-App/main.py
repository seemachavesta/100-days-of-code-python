from contact import Contact


    
class ContactManager:
  def __init__(self):
    self.contacts = {}
    
  
  def contact_exists(self, contact):
     return contact.name in self.contacts
   
   # add new contact information in contacts 
  def add_contact(self, contact):
    if self.contact_exists(contact):
      print(f"{contact.name} is already exists in contacts")
      return 
    
    self.contacts[contact.name]  = contact
    print(f"Contact '{contact.name}' added successfully.")
   
   
  def remove_contact(self, name):
    if name in self.contacts:
      del self.contacts[name]
      print(f"{name} has been deleted successfully.")
    else: 
      print(f"{name} does not exist in contacts.")
     
    
     
  def view_all_contacts(self):
    #check if contact list is empty
    if not  self.contacts:
      print("No contacts available.")
      return
    
    for contact in self.contacts.values():
      print(contact)
      print("-"*20)
     
  
  
  
contact1 = Contact('Rexy', '333-888-6946', 'test@yahoo.com', 'New Road, New York')
contact2 = Contact('Groega', '555-000-1800', 'george@test.com', 'Queens, New York')

contact_manager = ContactManager()
contact_manager.add_contact(contact1)
contact_manager.add_contact(contact2)





menu_prompt = f"Enter 'a', to add, 'r' to remove, 'l' to view all the contacts and 'q' to quit: "

while True:
  user_input = input(menu_prompt)
  if user_input == 'a':
    try:
      details = input("Enter name, phone number, email, and address (comma-separated): ")
      name, phone, email, address = map(str.strip, details.split(','))
      new_contact = Contact(name, phone, email, address)
      contact_manager.add_contact(new_contact)
    except ValueError:
      print("Invalid input format. Please provide details as: name, phone number, email, address.")
  elif user_input == 'r':
    name = input('Enter a contact name: ').title()
    contact_manager.remove_contact(name)
  elif user_input == 'l':
    contact_manager.view_all_contacts()
  elif user_input == 'q':
    break
  else:
    print('Invlid Choice')