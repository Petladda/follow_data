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
          default=AppRole.STUDENT
     )
     id_student = models.CharField(max_length=8)
     first_name = models.CharField(max_length=255)
     last_name =  models.CharField(max_length=255)
     def __str__(self):
          return str(self.username)

class Subject(models.Model):
     teacher = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     subject_name = models.CharField(max_length=255, default='')
    
     def __str__(self):
          return f"{self.subject_name}"

class Project(models.Model) :
     subject = models.ForeignKey(Subject , on_delete=models.SET_NULL, null=True,blank=True)
     members = models.ManyToManyField(AppUser)
     project_name = models.CharField(max_length=255, default='')
     trello_link = models.URLField(null=True,blank=True)
     figma_link = models.URLField(null=True,blank=True)
     
     def __str__(self) -> str:
          return f"{self.subject} - {self.pk}:{self.project_name}"



class ProductBacklog(models.Model):
     project = models.ForeignKey(Project , on_delete=models.SET_NULL, null=True,blank=True)
     title_product = models.CharField(max_length=255,default='')
     description = models.CharField(max_length=255,default='')
     date_to_do = models.DateField(default=datetime.date.today)
     hour_todo = models.IntegerField(default=0)
     STATUS_CHOICES = (
        ('todo', 'todo'),
        ('doing', 'doing'),
        ('done', 'done'),
     )
     status = models.CharField(max_length=5,choices=STATUS_CHOICES, default='todo')
     IM_CHOICES = (
        ('midium', 'midium'),
        ('low', 'low'),
        ('hight', 'hight'),
     )
     important = models.CharField(max_length=6, choices=IM_CHOICES, default='low')
     date_done = models.DateField(default=datetime.date.today)
     hour_done = models.IntegerField(default=0)


class Task(models.Model):
     product_backlog = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)
     task_id = models.CharField(max_length=255)
     task_name = models.CharField(max_length=255)
     id_student = models.CharField(max_length=8,null=True,blank=True)
     STATUS_CHOICES = (
        ('todo', 'todo'),
        ('doing', 'doing'),
        ('done', 'done'),
     )
     status = models.CharField(max_length=5,choices=STATUS_CHOICES, default='todo')
     date_to_do = models.DateField(default=datetime.date.today)
     date_done = models.DateField(default=datetime.date.today)
     hour_todo = models.IntegerField(default=0)
     hour_done = models.IntegerField(default=0)


class  DailyScrum(models.Model) :
     student =  models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     subject = models.ForeignKey(Subject,on_delete=models.SET_NULL, null=True,blank=True)
     project = models.ForeignKey(Project,on_delete=models.SET_NULL, null=True,blank=True)
     date = models.DateField(auto_now_add = True)
     yesterday = models.CharField(max_length=1000)
     today = models.CharField(max_length=1000)
     problem = models.CharField(max_length=1000)
     NOTE_CHOICES = [
     ('วันนี้ทำงาน', 'วันนี้ทำงาน'),
     ('ป่วย', 'ป่วย'),
     ('ติดธุระ', 'ติดธุระ'),
     ('ตกลงกันว่าวันนี้ไม่ทำงาน', 'ตกลงกันว่าวันนี้ไม่ทำงาน'),
     ]
     note = models.CharField(max_length=255, choices=NOTE_CHOICES)
     others = models.TextField(max_length=255)

     def __str__(self):
          return str(self.student)


    





