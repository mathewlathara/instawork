from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse  
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):  
   template = loader.get_template('index.html')
   return HttpResponse(template.render())