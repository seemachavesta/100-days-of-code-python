from pymongo import MongoClient
from bson import ObjectId
from teacher import  Teacher
from student import Student

class School:
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017/")
        db = client['school']
        self.teachers = db['teachers']
        self.students = db['students']
        self.classes = db['classes']


    def add_teachers(self, teacher: Teacher):
        result = self.teachers.insert_one(teacher.to_dict)
        return result.inserted_id

    def get_teacher_by_name(self, name):
        return self.teachers.find_one({'name': name})

    def remove_teacher(self, name_or_id):
        try:
            obj_id = ObjectId(name_or_id)
            result = self.teachers.delete_one({'_id': obj_id})
        except:
            result = self.teachers.delete_one({'name': name_or_id})

        if result.deleted_count == 0:
            print('No teacher found to delete')

        return result.deleted_count



    def add_student(self, student: Student):
        result = self.students.insert_one(student.to_dict)
        return result.inserted_id

    def get_student_by_name(self, name):
        return self.students.find_one({'name': name})


    def list_all_teachers(self):
        return list(self.teachers.find())


    def list_all_students(self):
        return list(self.students.find())


    def assign_teacher_to_class(self, teacher_name, class_name):
        return self.teachers.update_one({'name': teacher_name}, {'$set': {'assigned_class': class_name}})

    def enroll_student_in_class(self, student_name, class_name):
        return self.students.update_one({'name': student_name}, {'$set': {'enrolled_class': class_name}})

