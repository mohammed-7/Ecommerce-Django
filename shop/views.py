
# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render , redirect 

# def hello_world(request):
#     return HttpResponse("Hello, world! This is the shop app.")

def home(request):
    return render(request, 'shop/home.html')

def card(request):
    return render(request, 'shop/card.html')

def carousel(request):
    return render(request, 'shop/carousel.html')

def star(request):
    return render(request, 'shop/star.html')

def product(request):
    return render(request, 'shop/product.html')

def about(request):
    return render(request, 'shop/about.html')

def careers(request):
    return render(request, 'shop/careers.html')

def cart(request):
    return render(request, 'shop/cart.html')



def login(request):
    return render(request, 'shop/login.html')

