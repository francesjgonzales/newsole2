from django.shortcuts import render

from core.forms import ContactForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Shoe
def home(request):
    return render(request, 'home.html')

def shoe_list(request):
    items = Shoe.objects.all()  # Fetch all Shoe objects from the database
    return render(request, 'shoe_list.html', {"shoes": items})    

def shoe_detail(request, slug):
    shoe = Shoe.objects.get(slug=slug)  # Fetch the specific shoe by slug
    return render(request, 'shoe_detail.html', {"shoe": shoe})

def about(request):
    return render(request, 'about.html')

def add_to_cart(request):
    return render(request, 'cart.html')

@csrf_protect
def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect(reverse('home'))
        else:
            # Return the form with errors and user input preserved
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
        
    