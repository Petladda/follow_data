from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projectall.models import AppUser,Subject,Project,Student,DailyScrum,ProductBacklogs,Tasks

class SubjectAdmin(admin.ModelAdmin):
    list_display = ["subject_name","teacher"]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["group","student"]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["project_name","subject"]

class ProductBacklogsAdmin(admin.ModelAdmin):
    list_display = ["product","date_to_do","status","date_done","important"]

class DailyScrumAdmin(admin.ModelAdmin):
    list_display = ["student","date","yesterday","today","problem","note","others"]

class TasksAdmin(admin.ModelAdmin):
    list_display = ["product_backlogs","task_id","task_name","status"]
   
admin.site.register(AppUser,UserAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(DailyScrum,DailyScrumAdmin)
admin.site.register(ProductBacklogs,ProductBacklogsAdmin)
admin.site.register(Tasks,TasksAdmin)