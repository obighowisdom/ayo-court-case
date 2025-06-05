from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import CustomUser
from django.contrib.auth import get_user_model




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
