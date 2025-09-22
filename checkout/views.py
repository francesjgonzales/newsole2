from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from .models import UserPayment
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse  # new
from core.models import Shoe

stripe.api_key = settings.STRIPE_API_KEY
DOMAIN = settings.DOMAIN

# Create your views here.
def checkout(request):
    productId = request.POST.get('productId')


    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': "price_1S8jAD8QsB4BJQ5zQLTUcgLo" ,
                    'quantity': 1,
                    },
            ],
            payment_method_types=['card'],
            mode='payment',
            success_url=DOMAIN + '/success',
            cancel_url=DOMAIN + '/cancel',
        )
        return redirect(session.url, code=303)
    return render(request, 'checkout.html')


def success(request):
    return render(request, "success.html")


def cancel(request):
    return render(request, "cancel.html")

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            productId = request.POST.get('productId')
         
            checkout_session = stripe.checkout.Session.create(

                line_items=[
                    {
                        'price': "price_1S8jAD8QsB4BJQ5zQLTUcgLo" ,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=DOMAIN + '/success',
                cancel_url=DOMAIN + '/cancel',
            )
            
            return redirect(checkout_session.url)
        except Exception as error:
          
            return render (request,'public/error.html',{'error':error})

    return render(request, 'public/cancel.html')


@csrf_exempt 
def stripe_webhook(request):
  
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.WEBHOOK_ENDPOINT_SECRET
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError :
        return HttpResponse(status=400)

   
    if event['type'] == 'checkout.session.completed' :
        print(event)
        print('Payment was successful.') 
      

    
    return HttpResponse(status=200)