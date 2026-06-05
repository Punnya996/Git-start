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

