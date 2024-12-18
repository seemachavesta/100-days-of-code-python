#Student Management System
class Student:
  def __init__(self,student_id, name, age, grades):
    self.student_id = student_id
    self.name = name
    self.age = age
    self._grades = grades
    
 #prints student information 
  def __repr__(self):
    return f"Student Id: {self.student_id}, Name: {self.name}, Age: {self.age}, Grades: {self._grades}"

  #This function will display students grades for only read
  @property 
  def grade(self):
    return tuple(self._grades) 
    
#with this function we can add new grade in grade list
  @grade.setter
  def grade(self, new_grade):
    #if new grade is less then or equal to 0 or greater then 100
    if new_grade <= 0 or new_grade > 100:
      #program will raise a error message
      raise ValueError("Grade must be between 1 and 100.")

     # add new grade in grades list   
    self._grades.append(new_grade)

  #Calcualte student greades average
  @property 
  def calculate_average(self):
    if not self._grades:
      return 0.0
      
    average = sum(self._grades) / len(self._grades)
    return f"{average:.2f}"
  
 
   
class StudentManager:
  student_list = {}
  
  
  @classmethod 
  def add_student(cls, student):
    if student.student_id in cls.student_list:
      print(f'Student with ID {student.student_id} already exists.')
      return
    
    cls.student_list[student.student_id] = student
    
    
    
  @classmethod
  def display_students_list(cls):
    #loop over the student list 
    for student in cls.student_list.values():
      # print each students
      print(student)
    
  #This function return total number of students in list
  @classmethod   
  def total_students(cls):
    return f'There are {len(cls.student_list)} students'
    
    
    
    
    
mark = Student(1, 'Mark', 23, [65, 89, 55])
joe = Student(2, 'Joe', 20, [87, 98, 56])
maria = Student(2, 'Maria', 25, [55, 90, 76])

StudentManager.add_student(mark)
StudentManager.add_student(joe)
StudentManager.add_student(maria)


StudentManager.display_students_list()

print(StudentManager.total_students())

print(mark.grade)

# mark.grade  = -10

# print(mark.grade)
print(mark.calculate_average)