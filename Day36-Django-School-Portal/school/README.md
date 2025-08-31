# Day 36 — Django School Portal

A small Django project to practice clean data modeling, slug-based routing, template inheritance, and static assets. The app provides a simple portal to browse **Schools**, **Courses**, and **Students**, with a dashboard overview.

---

## What I Built

- **Dashboard**: counts for schools/courses/students and recent items.
- **Schools**
  - List page with course & student counts.
  - Detail page showing a school’s courses and students.
- **Courses**
  - List page with owning school and enrolled student count.
  - Detail page showing enrolled students.
- **Students**
  - Detail page with email, school, and enrolled courses.
- **Admin**
  - Registered models with improved list/search.
  - Slugs prepopulated from names for clean URLs.

---

## Domain Model

- `School (name, slug)`
- `Course (name, description, slug, school → ForeignKey)`
- `Student (student_name, email, slug, school → ForeignKey, courses → ManyToManyField(Course, related_name="students"))`

**Relationships**
- One **School** → many **Courses**  
- One **School** → many **Students**  
- Many **Students** ↔ many **Courses**

---

## What I Learned

- **Relational modeling in Django**
  - Using `ForeignKey` (one-to-many) and `ManyToManyField` (many-to-many).
  - Setting `related_name` to get natural reverse lookups like `school.students.all()` and `course.students.all()`.

- **URL design & slugs**
  - Slug-based detail routes (e.g., `/schools/<slug>/`, `/courses/<slug>/`) for readable URLs.
  - `get_object_or_404(Model, slug=slug)` for robust detail views.

- **Templates & structure**
  - Template inheritance with a base `layout.html`.
  - Avoiding content outside `{% block %}` when using `{% extends %}`.
  - Clean separation of concerns: HTML for structure, CSS in `static/` for styling.

- **Static files in development**
  - Correct per-app static layout: `enrollment/static/enrollment/style.css`.
  - Loading with `{% load static %}` and `<link rel="stylesheet" href="{% static 'enrollment/style.css' %}">`.

- **Admin productivity**
  - `list_display`, `search_fields`, `list_filter` for faster data management.
  - `prepopulated_fields` to auto-generate slugs.

- **Practical debugging**
  - Verifying M2M data via Django shell (`course.students.values_list(...)`) when lists render empty.
  - Catching CSS parse errors that break later rules.
  - Understanding why a child template’s `<link>` won’t render when it’s placed outside blocks.

---

## Tech Stack

- **Django** (4/5 compatible), **Python 3.10+**
- **SQLite** in development
- **Vanilla HTML/CSS** via Django static files

---

## How to Run (Dev)

```bash
# inside Day36-Django-School-Portal/
python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
