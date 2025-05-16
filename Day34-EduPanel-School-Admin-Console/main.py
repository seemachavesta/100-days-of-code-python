
from utils.student import Student
from utils.user import User
from utils.schoolAdminPanel import SchoolAdminPanel

panel = SchoolAdminPanel()


def add_user():
    username = input('Enter your username: ')
    role = input('Enter your Role: ').lower()
    user = User(username, role)
    return user

#Allow admin to add new student
def prompt_add_student(user):
    id = int(input("Enter student id: "))
    name = input("Enter student name: ")
    grade = input('Enter student grade: ')
    student = Student(id, name, grade)
    panel.add_student(user=user, student=student)

#Helper function for edit students record
def students_updates():
    updates = {}
    while True:
        field = input("What would you like to edit? (id, name, grade) or type 'done' to finish: ")
        if field == 'done':
            break

        if field not in ['id', 'name', 'grade']:
            print("Invalid field. Please enter 'id', 'name', or 'grade'.")
            continue
        new_value = input(f'Enter new value for {field}: ').strip()
        if field == 'id':
            if new_value.isdigit():
                updates['id'] = int(new_value)
            else:
                print('ID must be a number.')
        elif field == 'grade':
            updates['grade'] = new_value
        else:
            if new_value:
                updates['name'] = new_value
            else:
                print("Name field can't be empty. ")

    return updates

#Allow admin to edit student record
def prompt_edit_student(user):
    student_id = int(input('"Enter the ID of the student to edit: '))
    updates = students_updates()
    if updates:
        panel.edit_student(user=user, student_id=student_id, **updates)
    else:
        print('No changes were made.')

#This function allow admin to delete student using the student id
def prompt_delete_student(user):
    student_id = int(input('Enter the ID of the student to delete. '))
    panel.delete_student(user=user, student_id=student_id)


admin_menu = """
Welcome, Admin!
1. View Students
2. Add Student
3. Edit Student
4. Delete Student
5. Quit
"""

teacher_menu = """
Welcome, Teacher!
1. View Students
2. Quit
"""


def main():
    user = add_user()
    print(f"Welcome, {user.username}")
    while True:

        if user.role == 'admin':
            print(admin_menu)
            choice = int(input('Enter your selection: '))
            if choice == 1:
                panel.view_students(user=user)
            elif choice == 2:
                prompt_add_student(user)
            elif choice == 3:
                prompt_edit_student(user)
            elif choice == 4:
                prompt_delete_student(user)
            elif choice == 5:
                break
            else:
                print('Invalid choice')
        elif user.role == 'teacher':
            print(teacher_menu)
            choice = input("Enter your choice: ")

            if choice == '1':
                panel.view_students(user=user)
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")






if __name__ == '__main__':
    main()

