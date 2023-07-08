from django.shortcuts import render
from django.http import HttpResponse

def pqr(request):
    return render(request,'home.html')

def abc(request):
    return render(request,'about.html')

def mno(request):
    return render(request,'contec.html')

def xyz(request):
    return render(request,'main.html')

# Create your views here.
