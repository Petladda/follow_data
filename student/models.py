from django.db import models
from django.contrib.auth.models import User
from projectall.models import ProjectGroup

# Create your models here.
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     student_id = models.CharField(max_length=8, unique=True)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name} ({self.student_id})'