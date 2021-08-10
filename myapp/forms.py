from django import forms
from .models import Student
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.CharField(label="Username", required=True)
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput, required=True)


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ["first_name", "last_name", "username" , "email", "password"]


class StudentForm(forms.Form):
    code_chef_handle = forms.CharField(label="code_chef_handle", required=True)
    hacker_rank_handle = forms.CharField(label="hacker_rank_handle", required=False)
    code_forces_handle = forms.CharField(label="code_forces_handle", required=False)
    hacker_earth_handle = forms.CharField(label="hacker_earth_handle", required=False)
    roll_no = forms.CharField(label="roll_no", required=True)
    branch = forms.CharField(label="branch", required=True)
