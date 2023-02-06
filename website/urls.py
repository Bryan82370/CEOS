from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('addDocument/', views.addDocument, name='addDocument'),
    path('base/', views.base, name='base'),
    path('category/', views.category, name='category'),
    path('document/', views.document, name='document'),
]