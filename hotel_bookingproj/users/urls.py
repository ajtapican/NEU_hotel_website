from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]