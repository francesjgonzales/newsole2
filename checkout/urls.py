from django.urls import path
from . import views
import checkout.views
from .views import checkout, success, cancel

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
]