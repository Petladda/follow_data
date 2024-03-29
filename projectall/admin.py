from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projectall.models import *
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.utils.translation import gettext_lazy as _


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id","subject_name","teacher"]
    search_fields = ["subject_name"]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id","project_name","subject"]
    search_fields = ["project_name"]
    filter_horizontal = (
        "members",
    
    )

class ProductBacklogsAdmin(admin.ModelAdmin):
    list_display = ["id","project","date_to_do","status","date_done","important"]
    search_fields = ["project"]

class DailyScrumAdmin(admin.ModelAdmin):
    list_display = ["id","student","project","date","yesterday","today","problem","note","others"]

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id","product_backlog","task_id","task_name","status"]
    search_fields = ["task_id"]

class AppUserAdmin(UserAdmin):
    list_display = ("id","username", "email", "first_name", "last_name","role" ,"is_staff")


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

admin.site.register(StandUpMeeting,DailyScrumAdmin)
admin.site.register(ProductBacklog,ProductBacklogsAdmin)
admin.site.register(Task,TaskAdmin)