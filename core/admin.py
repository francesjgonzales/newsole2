from django.contrib import admin
from .models import ContactForm, Shoe, Wishlist, Cart

# Register your models here.
admin.site.register(Shoe)  # Registering the Shoe model to the admin site
admin.site.register(ContactForm)  # Registering the Contact model to the admin site
admin.site.register(Wishlist)  # Registering the Wishlist model to the admin site
admin.site.register(Cart)
