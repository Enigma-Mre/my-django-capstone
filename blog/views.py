from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'blog.html')

def header(request):
    return render(request, 'header.html')

def post(request):
    return render(request, 'post.html')