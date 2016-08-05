from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class CreatePersonForm(UserCreationForm):
    username = forms.EmailField(max_length=250, label='Email')


class PersonForm(AuthenticationForm):
    username = forms.EmailField(max_length=250, label='Email')
    password = forms.CharField(max_length=250, label='Password', widget=forms.PasswordInput)
