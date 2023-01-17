from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput({'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailField())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput({'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput({'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput({'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput({'class': 'form-input'}))