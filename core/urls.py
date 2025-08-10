from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoe_list, name='shoe_list'),
    path('cart/<int:shoe_id>/increase/', views.increase_quantity, 
    name='increase_quantity'),
    path('cart/<int:shoe_id>/decrease/', views.decrease_quantity, name='decrease_quantity'),

    path('shoe/<slug:slug>/', views.shoe_detail, name='shoe_detail'),
    path('contact/', views.contact_form, name='contact_form'),

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:shoe_id>/', views.add_to_cart, name='add_cart'),
    path('cart/remove/<int:shoe_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    path('checkout/', views.checkout, name='checkout')
]