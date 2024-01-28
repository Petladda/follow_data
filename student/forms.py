from django import forms
from .models import Student

from django.contrib.auth.forms import UserCreationForm

class StudentRegistrationForm(UserCreationForm):
    student_id = forms.CharField(max_length=8)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = Student
        fields = ['student_id', 'password1', 'password2', 'first_name', 'last_name', 'group']