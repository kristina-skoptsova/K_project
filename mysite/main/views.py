from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .form import *



def index(request):
    return render(request, 'main/index.html')

def profile(request):
    return render(request, 'main/profile.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    success_url = "main/login"
    template_name = 'register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items())) + list(c_def.items())

class LoginUser( LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items())) + list(c_def.items())
    def get_success_url(self):
        return reverse_lazy('home')