import contact
import contact_manager

user_menu = """
Enter:
- 'a' To add a new contact
- 'l' To list all contacts
- 's' To search for a contact by name
- 'd' To delete a contact by name
- 'q' To quit
Your choice: """


def prompt_add_contact(manager):
    name = input('Enter name: ')
    phone = input('Enter the phone number: ')
    email = input('Enter the email address: ')

    new_contact = contact.Contact(name, phone, email)
    manager.add_contact(new_contact)

def main():

    manager = contact_manager.ContactManager()

    while True:
        choice = input(user_menu).strip().lower()
        if choice == 'a':
            prompt_add_contact(manager)
        elif choice == 'l':
            manager.view_contacts()
        elif choice == 's':
            name = input('Enter the name you want to search: ').strip()
            manager.search_contact(name)
        elif choice == 'd':
            name = input('Enter the name to delete: ')
            manager.delete_contact(name)
        elif choice == 'q':
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()






