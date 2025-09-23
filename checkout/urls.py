from django.urls import path
from . import views
import checkout.views
from .views import checkout, checkout_success, checkout_cancel

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('checkout/cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),

]