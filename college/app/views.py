from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def btech(request):
    return render(request,'btech.html')

def mba(request):
    return render(request,'mba.html')

def diploma(request):
    return render(request,'diploma.html')

def pharmacy(request):
    return render(request,'pharmacy.html')