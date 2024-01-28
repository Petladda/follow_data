from django.contrib import admin

from student.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_id","first_name","last_name","group"]

admin.site.register(Student,StudentAdmin)