from django.contrib import admin
from .models import Course, Student, School

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'slug')
    list_filter = ('school', )
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'email', 'school', 'slug')
    list_filter = ('school',)
    search_fields = ('student_name', 'email',)
    prepopulated_fields = {'slug': ('student_name',)}




