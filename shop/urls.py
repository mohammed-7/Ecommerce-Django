from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.card, name='card'),
    path('', views.carousel, name='carousel'),
    path('', views.star, name='star'),
]
