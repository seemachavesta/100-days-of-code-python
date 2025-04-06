from flask import Flask, render_template, request, redirect, url_for
from teacher import Teacher
from student import Student
from school import School

app = Flask(__name__)

school = School()

@app.route('/')
def home():
    teacher_count = len(school.list_all_teachers())
    student_count = len(school.list_all_students())
    class_count = len(list(school.classes.find()))
    return render_template('home.html', teacher_count=teacher_count, student_count=student_count, class_count=class_count)

@app.route('/add-teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        teacher = Teacher(name, email, subject)
        school.add_teachers(teacher)
        return redirect(url_for('list_teachers'))
    return render_template('add_teacher.html')

@app.route('/teachers')
def list_teachers():
    teachers_data = school.list_all_teachers()
    teachers = []
    for t in teachers_data:
        teachers.append({
            'name': t.get('name'),
            'email': t.get('email'),
            'subject': t.get('subject'),
            'assigned_class': t.get('assigned_class')
        })
    return render_template('list_teachers.html', teachers=teachers)

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        grade = request.form['grade']
        student = Student(name, email, grade)
        school.add_student(student)
        return redirect(url_for('list_students'))
    return render_template('add_student.html')

@app.route('/students')
def list_students():
    students_data = school.list_all_students()
    students = []
    for s in students_data:
        students.append({
            'name': s.get('name'),
            'email': s.get('email'),
            'grade': s.get('grade'),
            'enrolled_class': s.get('enrolled_class')
        })
    return render_template('list_students.html', students=students)

@app.route('/assign-teacher', methods=['GET', 'POST'])
def assign_teacher():
    if request.method == 'POST':
        teacher_name = request.form['teacher_name']
        class_name = request.form['class_name']
        school.assign_teacher_to_class(teacher_name, class_name)
        return redirect(url_for('list_teachers'))
    return render_template('assign_teacher.html')

@app.route('/enroll-student', methods=['GET', 'POST'])
def enroll_student():
    if request.method == 'POST':
        student_name = request.form['student_name']
        class_name = request.form['class_name']
        school.enroll_student_in_class(student_name, class_name)
        return redirect(url_for('list_students'))
    return render_template('assign_student.html')

if __name__ == '__main__':
    app.run(debug=True)

