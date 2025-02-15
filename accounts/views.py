from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm 
from django.contrib.auth import get_user_model
from .forms import (CustomUserCreationForm, UserUpdateForm,)
from django.contrib.auth import get_user_model
from django.views.generic import (DetailView, UpdateView, DeleteView)
from django.urls import reverse 
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView) 
from django.contrib.auth.mixins import UserPassesTestMixin 
from .models import CustomUser

User = get_user_model()

class UserUpdate(UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'accounts/user_update.html'
    success_url = '/success-url/'
    
class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm 
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        login(self.request, user)
        return response
     
 
class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/user_detail.html'
    

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'accounts/user_detail.html'


class UserDelete(OnlyYouMixin, DeleteView):
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('login')