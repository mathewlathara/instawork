from django.shortcuts import render
from django.template import loader
from django.template import RequestContext, Template
from .models import Employee

# Create your views here.
from django.http import HttpResponse  
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):

   all_members = Employee.objects.all()
   totalcountofmembers = Employee.objects.all().count()
   """for i in all_members:
       print(i.first_name)"""
   print(totalcountofmembers)
   return render(request, 'index.html', {'members':all_members,'totalcountofmembers':totalcountofmembers})

def addmembers(request):
    user=request.user
    if request.method == "POST":
        #if user.is_authenticated:
        employee = Employee()
        employee.first_name = request.POST['firstname']
        employee.last_name = request.POST['lastname']
        employee.email = request.POST['emailid']
        employee.phone_number = request.POST['phone']
        employee.role_type = request.POST['memberole']
        employee.save()
        #firstname = request.POST['firstname'] #Using name of input
        #print(firstname)
        #Logic to save this email
        return render(request, 'index.html')
        """else:
            return render(request, "You are not Authenticated")"""
    else:
        return render(request,"index.html")
        