from django.shortcuts import render, redirect, get_object_or_404

from core.forms import ContactForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .utils import send_welcome_email

from .models import Shoe, Wishlist

def home(request):
    popular = Shoe.objects.filter(categories__contains='POPULAR')  # Fetch the specific shoe by ID
    return render(request, 'home.html', {"shoes": popular})

def about(request):
    return render(request, 'about.html')

def shoe_list(request):
    items = Shoe.objects.all()  # Fetch all Shoe objects from the database
    return render(request, 'shoe_list.html', {"shoes": items})    

def shoe_detail(request, slug):
    shoe = Shoe.objects.get(slug=slug)  # Fetch the specific shoe by slug
    return render(request, 'shoe_detail.html', {"shoe": shoe})

def add_to_cart(request, shoe_id):
    cart = request.session.get('cart', {})

    # Convert key to string for session storage
    shoe_id_str = str(shoe_id)

    if shoe_id_str in cart:
        cart[shoe_id_str] += 1
    else:
        cart[shoe_id_str] = 1
    
    # Save cart back to session
    request.session['cart'] = cart
    request.session.modified = True # mark session as changed

    return redirect('view_cart')  # redirect instead of rendering


def remove_from_cart(request, shoe_id):
    cart = request.session.get('cart', {})
    shoe_id_str = str(shoe_id)

    if shoe_id_str in cart:
        if cart[shoe_id_str] > 1:
            cart[shoe_id_str] -= 1  # decrease quantity by 1
        else:
            del cart[shoe_id_str]  # remove completely if quantity is 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_number = True if cart else False
    cart_number = bool(cart)

    shoes = Shoe.objects.filter(id__in=cart.keys())
    cart_total = 0

    for shoe in shoes:
        quantity = cart[str(shoe.id)]
        shoe.cart_quantity = quantity
        shoe.line_total = shoe.price * quantity
        cart_total += shoe.line_total

    return render(request, 'cart.html', {
        "shoes": shoes,
        "cart_total": cart_total,
        "cart_number": cart_number
    })
    
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

@login_required
def add_to_wishlist(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, shoe=shoe)

    if created:
        messages.success(request, f"{shoe.name} has been added to your wishlist!")
    else:
        messages.info(request, f"{shoe.name} is already in your wishlist.")

    return redirect('shoe_list')  # Change to where you want to redirect


# views.py
@login_required
def view_wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'items': items})

# views.py
def remove_from_wishlist(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, shoe=shoe).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, f"{shoe.name} has been removed from your wishlist.")
    else:
        messages.error(request, "Item not found in your wishlist.")

    return redirect('view_wishlist')


# Shoe Inventory
def increase_quantity(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    shoes = Shoe.objects.all()
    shoe.quantity += 1
    for shoe in shoes:
        shoe.total_price = shoe.price * shoe.quantity
    shoe.save()
    return render(request, 'cart.html', {'shoes': shoes})


def decrease_quantity(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    if shoe.quantity > 0:  # prevent negative stock
        shoe.quantity -= 1
        shoe.save()
    return redirect('cart')

# Basic user sign-up
@csrf_protect
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_welcome_email(user)

            # Send welcome email
            send_mail(
                subject="Welcome to Our Site!",
                message="Hi {},\n\nThanks for signing up! We're excited to have you onboard.".format(user.username),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            messages.success(request, "Your account has been created! Check your email for a welcome message.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})