from django.shortcuts import render

# Create your views here.
from .models import Blog

def home(request):
    return render(request, 'blog/home.html')