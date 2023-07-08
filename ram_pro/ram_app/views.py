from django.shortcuts import render
from django.http import HttpResponse

def xyz(request):
    return render(request,'abc.html')
# Create your views here.
