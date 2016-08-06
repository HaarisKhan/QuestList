from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class CreatePersonForm(UserCreationForm):
    username = forms.EmailField(max_length=250, label='Email', required=True)
    first_name = forms.CharField(max_length=250, label='First Name', required=True)
    last_name = forms.CharField(max_length=250, label="Last Name", required=True)


class PersonForm(AuthenticationForm):
    username = forms.EmailField(max_length=250, label='Email', required=True)
    password = forms.CharField(max_length=250, label='Password', widget=forms.PasswordInput, required=True)