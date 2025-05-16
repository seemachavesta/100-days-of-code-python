import functools


def access_control(allowed_roles):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, user, **kwargs):
            if user.role in allowed_roles:
                return func(self, user, **kwargs)
            else:
                raise PermissionError(
                    f"❌ Access denied for {user.username} ({user.role}) to {func.__name__}"
                )
        return wrapper
    return decorator


class SchoolAdminPanel:
    def __init__(self):
        self.students = []

    @access_control(["admin", "teacher"])
    def view_students(self, user):
        if not self.students:
            print( "No students available.")
            return
        for student in self.students:
            print(student)

    @access_control(['admin'])
    def add_student(self, user, student):
        new_student = student.to_dict
        for existing_student in self.students:
            if existing_student['id'] == new_student['id']:
                print(f"Student with ID {new_student['id']} already exists.")
                return
        self.students.append(new_student)
        print(f"Student {new_student['name']} added.")

    @access_control('admin')
    def edit_student(self, user, student_id, **updates):
        for student in self.students:
            if student.get('id') == student_id:
                allow_fields = ['id', 'name', 'grade']
                for key, value in updates.items():
                    if key in allow_fields:
                        student[key] = value
                print(f'Student with ID {student_id} updated.')
                return
        print('Student with ID {student_id} not found.')



    @access_control('admin')
    def delete_student(self, user, student_id):
        for student in self.students:
            if student['id'] == student_id:
                self.students.remove(student)
                print(f'Student with ID {student_id} deleted.')
                return
        print(f'Student with ID {student_id} not found.')
