from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm

class InscriptionForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur")

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2']

class ConnexionForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
