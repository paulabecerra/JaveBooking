#Forms for Users

#Django
from django import forms
from django.core.exceptions import ValidationError

#Models
from django.contrib.auth.models import User

#Signup Form
class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, label='Username')
    password = forms.CharField(
        max_length=70,
        label='Password',
        widget=forms.PasswordInput()
        )
    confirmation_password = forms.CharField(
        max_length=70, label='Password Confirmation',
        widget=forms.PasswordInput()
        )
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(label='Tu email Javeriana')

    def clean_email(self):
        data = self.cleaned_data['email']
        if 'javeriana.edu.co' not in data:
            raise forms.ValidationError('Debe ser un correo de la Universidad Javeriana')
        else:
            return data
