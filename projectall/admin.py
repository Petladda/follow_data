from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projectall.models import AppUser,Subject,Project,Student,DailyScrum,ProductBacklogs,Tasks
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.utils.translation import gettext_lazy as _


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["subject_name","teacher"]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["group","student"]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id","project_name","subject"]

    filter_horizontal = (
        "members",
    
    )

class ProductBacklogsAdmin(admin.ModelAdmin):
    list_display = ["product","date_to_do","status","date_done","important"]

class DailyScrumAdmin(admin.ModelAdmin):
    list_display = ["student","date","yesterday","today","problem","note","others"]

class TasksAdmin(admin.ModelAdmin):
    list_display = ["product_backlogs","task_id","task_name","status"]


class AppUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name","role" ,"is_staff")


    fieldsets = fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email","role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


    pass


admin.site.register(AppUser,AppUserAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(DailyScrum,DailyScrumAdmin)
admin.site.register(ProductBacklogs,ProductBacklogsAdmin)
admin.site.register(Tasks,TasksAdmin)