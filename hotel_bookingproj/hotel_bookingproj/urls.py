
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from pages.views import roompage_view
from pages.views import payment_view
from pages.views import fillup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name ='home'),
    path('users', include('users.urls')),
    path('roompage', roompage_view, name='roompage'),
    path('payment', payment_view, name='payment'),
    path('fillup', fillup_view, name='fillup'),
]
