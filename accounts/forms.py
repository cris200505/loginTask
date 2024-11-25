from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age']


class CustomUserCreationForm(UserCreationForm):
    """Formulario para la creación de un usuario personalizado."""
    
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'age')


class UserUpdateForm(forms.ModelForm):
    """Formulario para la actualización de datos del usuario."""
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age']
