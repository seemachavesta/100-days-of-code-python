from django.db import models


class School(models.Model):
    name = models.CharField( max_length=100)
    address = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    school = models.ForeignKey(
        School, 
        on_delete=models.PROTECT,
        related_name='courses'
        )
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self):
        return self.name


class Student(models.Model):
    student_name = models.CharField( max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField(Course, related_name="students")
    school = models.ForeignKey(
        School, 
        on_delete=models.PROTECT,
        related_name='students'
        )
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self) -> str:
        return f'{self.student_name} ({self.email})'



    

    