from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html')

def im_hungry(request):
    return render(request, 'shopping.html')

def index(request):
    return render(request, 'index.html')