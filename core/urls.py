from django.urls import path
from django.contrib.auth import views as auth_views
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
    
    path('checkout/', views.checkout, name='checkout'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('wishlist/add/<int:shoe_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    path('wishlist/remove/<int:shoe_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    path('wishlist/', views.view_wishlist, name='view_wishlist'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]