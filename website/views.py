from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'security/login.html')

def register(request):
    return render(request, 'security/register.html')

def addCategory(request):
    return render(request, 'addCategory.html')

def addDocument(request):
    return render(request, 'addDocument.html')

def document(request):
    return render(request, 'document.html')

def category(request):
    return render(request, 'category.html')