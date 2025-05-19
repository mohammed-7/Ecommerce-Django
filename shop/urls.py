from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.card, name='card'),
    path('', views.carousel, name='carousel'),
    path('', views.star, name='star'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('cart/', views.cart, name='cart'),
    
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
