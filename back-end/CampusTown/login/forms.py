from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class LoginForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','is_staff','password']
