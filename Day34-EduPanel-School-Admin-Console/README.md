# 🎓 School Admin Panel - Day 34 of 100 Days of Python

Welcome to **Day 34** of my **100 Days of Python** challenge!  
This project is a command-line based **School Administration Panel** with **role-based access control**, developed using core Python principles like decorators, class-based design, and dynamic user input handling.

---

## 🚀 Features

**Role-based Access Control** (`admin`, `teacher`)
-   Admin Capabilities:
  - View student list
  - Add new student
  - Edit existing student details
  - Delete a student
-  Teacher Capabilities:
  - View student list
-  Unauthorized access results in a `PermissionError`

---

##  Project Structure
├── main.py # Entry point for CLI interaction
├── test_school_admin_panel.py # Unit tests using unittest
└── utils/
├── schoolAdminPanel.py # Core business logic and access control
├── student.py # Student model
└── user.py # User model

 Learning Highlights (Day 34)
✅ Writing decorators for access control

✅ Organizing code with classes and modules

✅ Dynamic CLI with input()

✅ Using @property to format data

✅ Writing robust unit tests with unittest



