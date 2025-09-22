from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserPayment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255)
    stripe_checkout_session_id = models.CharField(max_length=255, blank=True, null=True)    
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    shoe_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.shoe_name} - {'Paid' if self.has_paid else 'Pending'}"