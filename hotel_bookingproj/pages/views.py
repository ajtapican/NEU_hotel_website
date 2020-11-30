from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from pages.models import Information
from pages.forms import Info

# Create your views here.


# for testing code  no html
#def home_view(request, *args, **kwargs):
 #   return HttpResponse("<h1> home page </h1> ")



# html of home.html

def home_view(request, *args, **kwargs):
   print(args, kwargs)
   print(request.user)
   return render(request, 'home.html', {})

@login_required
def roompage_view(request, *args, **kwargs):
   print(args, kwargs)
   print(request.user)
   return render(request, 'room page2.html', {})

@login_required
def fillup_view(request, *args, **kwargs):
   print(args, kwargs)
   print(request.user)
   return render(request, 'fillup.html', {})

@login_required
def payment_view(request, *args, **kwargs):
   print(args, kwargs)
   print(request.user)
   if request.method == "POST":
      form = Info(request.POST or None)
      if form.is_valid():
         form.save()
         return redirect('home')
   else:
      return render(request, 'payment.html', {})

