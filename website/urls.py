from django.urls import path
from .views import logout_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('nav/', views.nav, name='nav'),
    path('register/', views.register, name='register'),
    path('addDocument/', views.addDocument, name='addDocument'),
    path('addDemarche/', views.addDemarche, name='addDemarche'),
    path('addTask/', views.addTask, name='addTask'),
    path('base/', views.base, name='base'),
    path('step/', views.step, name='step'),
    path('document/', views.document, name='document'),
    path('info/', views.info, name='info'),
    path('about/', views.about, name='about'),
    path('about_logout/', views.about_logout, name='about_logout'),
    path('list/', views.list, name='list'),
    path('choise/', views.choise, name='choise'),
    path('logout/', logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('see_file/', views.see_file, name='see_file'),
]