from django.http import HttpResponse 
from django.shortcuts import render


# Create your views here.




def index(request):
    return render(request,"hello/index.html")

def fahad(request):
    return HttpResponse("Hwllo! Fahad babu 🏊")

def faiz(request):
    return HttpResponse("Hello! Faiz babau 🐊")

def faisal(request):
    return HttpResponse("Hello! Faisal babau 🐍")

def greet(request ,name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })