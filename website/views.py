from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm
from django.shortcuts import render, redirect
from .models import Utilisateur
from django.contrib import messages
from .forms import ConnexionForm
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
from django.core.cache import cache


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def choise(request):
    return render(request, 'security/choise.html')

def user_login(request):
    if request.method == 'POST':
        form = ConnexionForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                form.add_error(None, 'Identifiants invalides')
    else:
        form = ConnexionForm()
    return render(request, 'security/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = InscriptionForm()
    return render(request, 'security/register.html', {'form': form})

@login_required(login_url='index.html')
def addCategory(request):
    return render(request, 'addCategory.html')

@login_required(login_url='index.html')
def addDocument(request):
    return render(request, 'documents/addDocument.html')

@login_required(login_url='index.html')
def addTask(request):
    return render(request, 'addTask.html')

@login_required(login_url='index.html')
def addDemarche(request):
    return render(request, 'addDemarche.html')

@login_required(login_url='index.html')
def document(request):
    return render(request, 'documents/document.html')

@login_required(login_url='index.html')
def step(request):
    return render(request, 'step.html')

@login_required(login_url='index.html')
def info(request):
    return render(request, 'info.html')

@login_required(login_url='index.html')
def about(request):
    return render(request, 'about.html')

def about_logout(request):
    return render(request, 'about_logout.html')

@login_required(login_url='index.html')
def list(request):
    return render(request, 'list.html')

def logout_view(request):
    logout(request)
    cache.clear()
    return redirect('index.html')

@login_required(login_url='index.html')
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='index.html')
def see_file(request):
    return render(request, 'documents/see_file.html')

def nav(request):
    return render(request, 'nav.html')
