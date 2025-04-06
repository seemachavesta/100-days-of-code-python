from school import School
from teacher import Teacher
from student import Student

def main():
    school = School()

    while True:
        print("\n1. Add Teacher\n2. List Teachers\n3. Remove Teacher\n0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            subject = input("Subject: ")
            teacher = Teacher(name, email, subject)
            school.add_teachers(teacher)
        elif choice == "2":
            for t in school.list_all_teachers():
                print(t)
        elif choice == "3":
            name = input("Enter teacher name or ID to remove: ")
            school.remove_teacher(name)
        elif choice == "0":
            break

if __name__ == '__main__':
    main()





