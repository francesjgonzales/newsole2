from django.shortcuts import render

from core.forms import ContactForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Shoe

def home(request):
    latest = Shoe.objects.filter(categories='POPULAR')  # Fetch the specific shoe by ID
    return render(request, 'home.html', {"shoes": latest})

def about(request):
    return render(request, 'about.html')

def shoe_list(request):
    items = Shoe.objects.all()  # Fetch all Shoe objects from the database
    return render(request, 'shoe_list.html', {"shoes": items})    

def shoe_detail(request, slug):
    shoe = Shoe.objects.get(slug=slug)  # Fetch the specific shoe by slug
    return render(request, 'shoe_detail.html', {"shoe": shoe})

def add_to_cart(request, shoe_id):
    cart = request.session.get('cart', [])
    if shoe_id not in cart:
        cart.append(shoe_id)
    request.session['cart'] = cart
    return render(request, 'cart.html', {"shoes": Shoe.objects.filter(id__in=cart)})

def remove_from_cart(request, shoe_id):
    cart = request.session.get('cart', [])
    if shoe_id in cart:
        cart.remove(shoe_id)
    request.session['cart'] = cart
    return render(request, 'cart.html', {"shoes": Shoe.objects.filter(id__in=cart)})

def view_cart(request):
    cart = request.session.get('cart', [])
    shoes = Shoe.objects.filter(id__in=cart)
    grand_price = sum(shoe.price for shoe in shoes) if shoes else 0.00
    return render(request, 'cart.html', {"shoes": shoes, "grand_price": grand_price})

def checkout(request):
    checkout = request.session.get('cart', [])
    shoes = Shoe.objects.filter(id__in=checkout)
    # total_price = sum(shoe.price for shoe in shoes)
    total_price = sum(shoe.price for shoe in shoes) if shoes else 0.00

    return render(request, 'checkout.html', {"shoes": shoes, "total_price": total_price})

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
        
    