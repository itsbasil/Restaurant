from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def location(request):
    return render(request,'location.html')
def menu(request):
    return render(request,'menu.html')