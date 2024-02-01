import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 

class AppRole(models.TextChoices) :
     STUDENT = "STD", _("Student")
     TEACHER = "TCH", _("Teacher")

class AppUser(AbstractUser) :
     role = models.CharField(
          max_length=255,
          choices=AppRole.choices,
     )
     id_student = models.CharField(max_length=8)
     first_name = models.CharField(max_length=255)
     last_name =  models.CharField(max_length=255)

class Subject(models.Model):
     teacher = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     subject_name = models.CharField(max_length=255, default='')
    
     def __str__(self):
          return str(self.subject_name)

class Project(models.Model) :
     subject = models.ForeignKey(Subject , on_delete=models.SET_NULL, null=True,blank=True)
     users = models.ManyToManyField(AppUser)
     project_name = models.CharField(max_length=255, default='')
     trello_link = models.URLField(null=True,blank=True)
     figma_link = models.URLField(null=True,blank=True)

class Student(models.Model):
     student =  models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     group = models.ForeignKey(Subject , on_delete=models.SET_NULL, null=True,blank=True)
    


class ProductBacklogs(models.Model):
     product = models.ForeignKey(Project , on_delete=models.SET_NULL, null=True,blank=True)
     title_product = models.CharField(max_length=255,default='')
     date_to_do = models.DateField(default=datetime.date.today)
     STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
     )
     status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='todo')
     date_done = models.DateField(default=datetime.date.today)
     IM_CHOICES = (
        ('low', 'ต่ำ'),
        ('mid', 'ปานกลาง'),
        ('hight', 'มาก'),
     )
     important = models.CharField(max_length=5, choices=IM_CHOICES, default='low')


class  DailyScrum(models.Model) :
     student =  models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     date = models.DateField(auto_now_add = True)
     yesterday = models.CharField(max_length=1000)
     today = models.CharField(max_length=1000)
     problem = models.CharField(max_length=1000)
     NOTE_CHOICES = [
     ('work', 'วันนี่ทำงาน'),
     ('sick', 'ป่วย'),
     ('busy', 'ติดธุระ'),
     ('pass', 'ตกลงกันว่าวันนี้ไม่ทำงาน'),
     ]
     note = models.CharField(max_length=4, choices=NOTE_CHOICES)
     others = models.TextField(max_length=255)

     def __str__(self):
          return str(self.student)

class Tasks(models.Model):
     product_backlogs = models.ForeignKey(ProductBacklogs, on_delete=models.CASCADE)
     task_id = models.CharField(max_length=255)
     task_name = models.CharField(max_length=255)
     STATUS_CHOICES = (
          ('todo', 'To Do'),
          ('doing', 'Doing'),
          ('done', 'Done'),
     )
     status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='todo')


"""
class Student(models.Model):
     student =  models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     student_id = models.CharField(max_length=8)
     first_name = models.CharField(max_length=255)
     last_name =  models.CharField(max_length=255)
     

class  DailyScrum(models.Model) :
     student =  models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     date = models.DataField(auto_now_add = True)
     yesterday = models.CharField(max_length=1000)
     today = models.CharField(max_length=1000)
     problem = models.CharField(max_length=1000)
     NOTE_CHOICES = [
     ('work', 'วันนี่ทำงาน'),
     ('sick', 'ป่วย'),
     ('busy', 'ติดธุระ'),
     ('pass', 'ตกลงกันว่าวันนี้ไม่ทำงาน'),
     ]
     note = models.CharField(max_length=4, choices=NOTE_CHOICES)
     others = models.TextField(max_length=255)

class ProductBacklogs(models.Model):
     product = models.ForeignKey(Project , on_delete=models.SET_NULL, null=True,blank=True)
     #name_backlog = models.CharField(max_length=255,default='')
     date_to_do = models.DateField(default=datetime.date.today)
     STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
     )
     status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='todo')
     date_done = models.DateField(default=datetime.date.today)
     IM_CHOICES = (
        ('low', 'ต่ำ'),
        ('mid', 'ปานกลาง'),
        ('hight', 'มาก'),
     )
     important = models.CharField(max_length=5, choices=IM_CHOICES, default='low')
class Tasks(models.Model):
     product_backlog = models.ForeignKey(ProductBacklogs, on_delete=models.CASCADE)
     task_id = models.CharField(max_length=255)
     task_name = models.CharField(max_length=255)
     '''STATUS_CHOICES = (
          ('todo', 'To Do'),
          ('doing', 'Doing'),
          ('done', 'Done'),
     )'''
     status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='todo')
"""

