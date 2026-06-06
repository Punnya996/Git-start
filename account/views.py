from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstExample(request,*args,**kwargs):
    return HttpResponse("Request is here")

def secondExample(request):
    return HttpResponse("<h1>Hi HTTP </h1>")

def homeView(request):
    return render(request,"home.html")

def aboutView(request):
    return render(request,"about.html")

def worksView(request):
    username="amalkrishna"
    services=["web development","photography","caretaker","nurse"]
    works=[{"id":1,"name":"abu","dept":"cse","age":32},
            {"id":2,"name":"vinu","dept":"eee","age":31},
            {"id":3,"name":"manu","dept":"mech","age":30},
            {"id":4,"name":"kavu","dept":"civil","age":39}]
    return render(request,"works.html",{"uname":username,"service_list":services,"works":works})

def addWorksView(request):
    return render(request,"addworks.html")


