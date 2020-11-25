
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from pages.views import roompage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name ='home'),
    path('users', include('users.urls')),
    path('roompage', roompage_view, name='roompage'),
]
