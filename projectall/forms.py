
from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import AppUser


class  RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = UserCreationForm.Meta.fields 

class SubjectForm(forms.Form):
    subject = forms.CharField(max_length=255)
    project_count = forms.IntegerField()


