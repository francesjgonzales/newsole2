import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from .models import UserPayment
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Shoe

stripe.api_key = settings.STRIPE_API_KEY
DOMAIN = settings.DOMAIN

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    shoes = Shoe.objects.filter(id__in=cart.keys())
    line_items = []
    all_items = []

    for shoe in shoes:
        qty = cart[str(shoe.id)]

        item = {
            'price': shoe.stripe_price_id,
            'quantity': qty,
        }

        if not shoe.stripe_price_id:
            raise Exception(f"Product {shoe.name} is not available for purchase.")
        
        line_items.append(item)
        all_items.append({
            'price': shoe.stripe_price_id,
            'quantity': qty,
        })
    
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=DOMAIN + '/checkout/success',
        cancel_url=DOMAIN + '/cart',
    )
    print(line_items)
    return redirect(checkout_session.url, code=303)

def checkout_success(request):
    return render(request, "checkout_success.html")

def checkout_cancel(reverse):
    return render(reverse, "cart.html")


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    # Handle only successful checkout sessions
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        checkout_session_id = session['id']
        # Locate UserPayment by checkout session id
        try:
            user_payment = UserPayment.objects.get(stripe_checkout_session_id=checkout_session_id)
            user_payment.has_paid = True
            user_payment.save()
        except UserPayment.DoesNotExist:
            pass  # Optionally log this
    
    return HttpResponse(status=200)
