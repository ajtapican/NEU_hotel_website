
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import roompage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name ='home'),
    path('roompage', roompage_view, name='roompage'),
]
