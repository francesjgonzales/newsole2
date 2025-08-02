from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoe_list, name='shoe_list'),
    path('shoe/<slug:slug>/', views.shoe_detail, name='shoe_detail'),
    path('contact/', views.contact_form, name='contact_form'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]