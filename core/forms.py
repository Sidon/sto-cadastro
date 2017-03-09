from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')

