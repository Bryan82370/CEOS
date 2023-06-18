from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm

class InscriptionForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'style': 'border-radius: 20px; width: 100%;'}), label="Nom d'utilisateur")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'border-radius: 20px; width: 100%;'}), label="Nom d'utilisateur")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'border-radius: 20px; width: 100%;'}), label="Nom d'utilisateur")

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2']

class ConnexionForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'style': 'border-radius: 20px; width: 100%;'}), label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'border-radius: 20px; width: 100%;'}), label="Mot de passe")
