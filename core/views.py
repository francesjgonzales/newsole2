
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from core.forms import ContactForm, LoginForm, SignUpForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth import login, authenticate
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .utils import send_welcome_email

from .models import Shoe, Wishlist, Cart
from django.db.models import Q
from django.core.paginator import Paginator

# Home functionality
def home(request):
    popular = Shoe.objects.filter(categories__contains='POPULAR')  # Fetch the specific shoe by ID
    return render(request, 'home.html', {"shoes": popular})

def about(request):
    return render(request, 'about.html')

def shoe_list(request):
    items = Shoe.objects.all()  # Fetch all Shoe objects from the database
  # Pagination can be added here if needed
    paginator = Paginator(items, 5)  # Show 5 shoes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shoe_list.html', {"shoes": items, 'page_obj': page_obj})    

def shoe_detail(request, slug):
    shoe = Shoe.objects.get(slug=slug)  # Fetch the specific shoe by slug
    return render(request, 'shoe_detail.html', {"shoe": shoe})

def shoe_search(request):
    query = request.GET.get('q')  # Get the search term from URL query params
    if query:
        shoes = Shoe.objects.filter(name__icontains=query)  # Case-insensitive search
    else:
        shoes = Shoe.objects.all()  # Show all shoes if no search query
    return render(request, 'search.html', {'shoes': shoes, 'query': query})

# Wishlist functionality
@login_required(login_url='login')
def add_to_wishlist(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, shoe=shoe)

    if created:
        messages.success(request, f"{shoe.name} has been added to your wishlist!")
    else:
        messages.info(request, f"{shoe.name} is already in your wishlist.")

    return redirect('shoe_list')  # Change to where you want to redirect

@login_required(login_url='login')
def view_wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'items': items})

def remove_from_wishlist(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, shoe=shoe).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.warning(request, f"{shoe.name} has been removed from your wishlist.")
    else:
        messages.error(request, "Item not found in your wishlist.")

    return redirect('view_wishlist')


# Cart functionality
@login_required(login_url='login')
def add_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, shoe=shoe)
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


@login_required(login_url='login')
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

def remove_from_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    cart_item = Cart.objects.filter(user=request.user, shoe=shoe).first()

    if cart_item:
        cart_item.delete()
        messages.success(request, f"{shoe.name} has been removed from your cart.")
    else:
        messages.error(request, "Item not found in your cart.")

    # Update session cart
    # Ensure the cart is a dictionary
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    # Convert shoe_id to string for session storage
    shoe_id_str = str(shoe_id)
    cart = request.session['cart']

    if shoe_id_str in cart:
        if cart[shoe_id_str] > 1:
            cart[shoe_id_str] -= 1  # decrease quantity by 1
        else:
            del cart[shoe_id_str]  # remove completely if quantity is 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('view_cart')

def remove_all_from_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    cart_item = Cart.objects.filter(user=request.user, shoe=shoe).first()

    if cart_item:
        cart_item.delete()
        messages.success(request, f"{shoe.name} has been removed from your wishlist.")
    else:
        messages.error(request, "Item not found in your wishlist.")

    # Update session cart
    # Ensure the cart is a dictionary
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    # Convert shoe_id to string for session storage
    shoe_id_str = str(shoe_id)
    cart = request.session['cart']

    if shoe_id_str in cart:
        del cart[shoe_id_str]  # remove completely if quantity is 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('view_cart')

# Move Wishlist to Cart functionality
@login_required(login_url='login')
def move_wishlist_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, shoe=shoe).first()
    
    if wishlist_item:
        wishlist_item.delete()  # Remove from wishlist
        messages.success(request, f"{shoe.name} has been moved to your cart.")
    else:
        messages.error(request, "Item not found in your wishlist.")
    
    cart_item, created = Cart.objects.get_or_create(user=request.user, shoe=shoe)
    if not created:
        cart_item.shoe_id += 1
        cart_item.save()

    cart = request.session.get('cart', {})
    shoe_id_str = str(shoe_id)
    
    if shoe_id_str in cart:
        cart[shoe_id_str] += 1
    else:
        cart[shoe_id_str] = 1
    
    request.session['cart'] = cart
    request.session.modified = True  # mark session as changed

    return redirect('view_cart')

# Move Cart to Wishlist functionality
@login_required(login_url='login')
def move_cart_to_wishlist(request, shoe_id):
    cart = request.session.get('cart', {})
    shoe_id_str = str(shoe_id)

    if shoe_id_str in cart:
        del cart[shoe_id_str]  # Remove from cart
        request.session['cart'] = cart
        request.session.modified = True # mark session as changed
        shoe = get_object_or_404(Shoe, id=shoe_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, shoe=shoe)

        if created:
            messages.success(request, f"{shoe.name} has been moved to your wishlist!")
        else:
            messages.info(request, f"{shoe.name} is already in your wishlist.")
    else:
        messages.error(request, "Item not found in your cart.")

    return redirect('view_wishlist')

def activateEmail(request):
    user = request.user
    send_welcome_email(user)
    messages.success(request, "A welcome email has been sent to your email address.")
    return redirect('home')

# User Signup
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_welcome_email(user)  # Send welcome email
            messages.success(request, "Account created successfully! A welcome email has been sent to your email address.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# Contact Form
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
            messages.warning(request, "Please correct the errors below.")
            return render(request, 'contact.html', {'contactform': form})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'contactform': form})


# Login Form
@csrf_protect
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('shoe_list')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

