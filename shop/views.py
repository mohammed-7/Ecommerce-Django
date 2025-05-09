
# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render , redirect 

# def hello_world(request):
#     return HttpResponse("Hello, world! This is the shop app.")

def home(request):
    return render(request, 'shop/base.html')

def card(request):
    return render(request, 'shop/card.html')

def carousel(request):
    return render(request, 'shop/carousel.html')

def star(request):
    return render(request, 'shop/star.html')

