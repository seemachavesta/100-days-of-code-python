import unittest
from utils.schoolAdminPanel import SchoolAdminPanel
from utils.student import Student
from utils.user import User


class TestSchoolAdminPanel(unittest.TestCase):

    def setUp(self):
        self.panel = SchoolAdminPanel()
        self.admin_user = User("admin1", "admin")
        self.teacher_user = User("teacher1", "teacher")
        self.student1 = Student(1, "John Doe", "A")
        self.student2 = Student(2, "Jane Smith", "B")

    def test_admin_can_add_student(self):
        self.panel.add_student(user=self.admin_user, student=self.student1)
        self.assertEqual(len(self.panel.students), 1)
        self.assertEqual(self.panel.students[0]['name'], "John Doe")

    def test_teacher_cannot_add_student(self):
        with self.assertRaises(PermissionError):
            self.panel.add_student(user=self.teacher_user, student=self.student1)

    def test_admin_can_view_students(self):
        self.panel.add_student(user=self.admin_user, student=self.student1)
        try:
            self.panel.view_students(user=self.admin_user)
        except Exception as e:
            self.fail(f"view_students raised an exception unexpectedly: {e}")

    def test_teacher_can_view_students(self):
        self.panel.add_student(user=self.admin_user, student=self.student1)
        try:
            self.panel.view_students(user=self.teacher_user)
        except Exception as e:
            self.fail(f"view_students raised an exception for teacher: {e}")

    def test_edit_student(self):
        self.panel.add_student(user=self.admin_user, student=self.student1)
        self.panel.edit_student(user=self.admin_user, student_id=1, name="Johnny")
        self.assertEqual(self.panel.students[0]['name'], "Johnny")

    def test_delete_student(self):
        self.panel.add_student(user=self.admin_user, student=self.student1)
        self.panel.delete_student(user=self.admin_user, student_id=1)
        self.assertEqual(len(self.panel.students), 0)

    def test_add_duplicate_student(self):
        self.panel.add_student(user=self.admin_user, student=self.student1)
        self.panel.add_student(user=self.admin_user, student=self.student1)
        self.assertEqual(len(self.panel.students), 1)


if __name__ == '__main__':
    unittest.main()
