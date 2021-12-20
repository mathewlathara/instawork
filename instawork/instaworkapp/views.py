from django.shortcuts import render
from django.template import loader
from django.template import RequestContext, Template

# Create your views here.
from django.http import HttpResponse  
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):  
   template = loader.get_template('index.html')
   return render(request, 'index.html')

def addmembers(request):
    user=request.user
    if request.method == "POST":
        #if user.is_authenticated:
        firstname = request.POST['firstname'] #Using name of input
        print(firstname)
        #Logic to save this email
        return render(request, 'index.html')
        """else:
            return render(request, "You are not Authenticated")"""
    else:
        return render(request,"index.html")