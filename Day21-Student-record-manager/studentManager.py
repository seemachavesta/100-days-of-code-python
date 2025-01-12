import json
from student import Student
       
class StudentManager:
    # Manages a collection of students, including adding, deleting, and filtering them
    def __init__(self, file_name='students.json'):
        self.file_name = file_name
        self.students = self.load_file()
        
    def load_file(self):
        """Load student data from json file"""
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except FileNotFoundError:
            print("Error File not found. starting with an empty list.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON file. Starting with an empty list.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

            
    def save_to_file(self):
        """Save the current list of students to the JSON file."""
        with open(self.file_name, 'w') as file:
            json.dump(self.students, file, indent=4)

            
    def add_subjects(self, student,subject, grade):
        # Adds or updates a subject for an existing student
        for entry in student['subjects']:
            if entry['subject'] == subject:
                print(f"Subject {subject} already exists for student. Updating grade.")
                entry['grade'] = grade
                self.save_to_file()
                return
         # Append the subject only if it doesn't exist
        student['subjects'].append({'subject': subject, 'grade': grade})
        self.save_to_file()
                    
     
    def add_student(self,id, name, subject, grade):
        """Add a new student or update an existing one."""
        if not isinstance(id, int) or not name or not subject or not isinstance(grade, (int, float)):
            print("Invalid input. Please provide valid data.")
            return
        
        # Check if the student already exists
        for student in self.students:
            if student['id'] == id:
                self.add_subjects(student, subject, grade)
                return
            
        # Add a new student if not found       
        new_student = Student(id, name)
        new_student.add_subject(subject, grade)
        self.students.append(new_student.to_dict())
        self.save_to_file()
        print(f"Added new student: {name}")
        
          
    def view_students(self):
        """Displays all students and their subjects."""
        if not self.students:
            print('There is no record to display')
            return
        
        for student in self.students:
            print(f"ID: {student['id']}, Name: {student['name']}")
            for subject in student['subjects']:
                print(f"  Subject: {subject['subject']}, Marks: {subject['grade']}")
            print('-' * 30)
                
                          
    def grade_result(self,student,result):
        """Helper function to format the filtered results."""
        results = []
        for subject in result:
            results.append({
                    'name': student['name'],
                    'subject': subject['subject'],
                    'grade': subject['grade']
                })
                
        return results
                
                
    def filter_subjects(self, condition):
        """Filters subjects based on a condition."""
        result = []
        for student in self.students:
            filterd = filter(condition, student['subjects'])
            result.extend(self.grade_result(student, filterd))
            
        return result
        
   
    def filter_passed_subjects(self):
        """Filters and displays all subjects where grades are >= 50."""
        passed_subjects = self.filter_subjects(lambda subject: subject['grade'] >= 50)
        if not passed_subjects:
            print('No result found.')
            return
        
        print("Passing Subjects:")
        for entry in passed_subjects:
            print(f"Student: {entry['name']}, Subject: {entry['subject']}, Grade: {entry['grade']}")
            
                    
    def filter_failed_subjects(self):
        """Filters and displays all subjects where grades are < 50."""
        failed_subjects = self.filter_subjects(lambda subject: subject['grade'] < 50)
                    
        if not failed_subjects:
            print('No failed subjects found')
            return
        
        print('Failed Subjects')
        for entry in failed_subjects:
            print(f"Student: {entry['name']}, Subject: {entry['subject']}, Grade: {entry['grade']}")

                
    def delete_student(self, id):
        """Deletes a student by their ID."""
        for student in self.students:
            if student['id'] == id:
                self.students.remove(student)
                self.save_to_file()
                print(f"Student {student['name']} with ID {id} has been deleted successfully.")
                return
        
        print(f"No student found with ID {id}.")

            
      
        
                
                
manager = StudentManager()

manager.add_student(1, 'Rayan', 'Math', 60)
manager.add_student(1, 'Rayan', 'English', 40)
manager.add_student(2, 'Maria', 'English', 70)
manager.add_student(3, 'Alis', 'English', 98)
manager.add_student(3, 'Alis', 'Science', 75)



# manager.filter_passed_subjects()
# manager.filter_failed_subjects()

# manager.delete_student(2)

manager.view_students()