from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')