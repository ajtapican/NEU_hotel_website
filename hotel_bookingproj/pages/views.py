from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
