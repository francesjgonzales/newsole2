import stripe
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Shoe

stripe.api_key = settings.STRIPE_API_KEY

class Command(BaseCommand):
    help = "Seed Shoe data to Stripe (create products & prices on Stripe for each Shoe)"

    def handle(self, *args, **options):
        stripe.api_key = settings.STRIPE_API_KEY

        for shoe in Shoe.objects.all():
            if not shoe.stripe_product_id:
                print(f"Creating Stripe product for {shoe.name}...")
                # Create product
                product = stripe.Product.create(
                    name=shoe.name,
                    description=shoe.description,
                    images=[shoe.image.url] if shoe.image else None,
                )
                shoe.stripe_product_id = product.id
            else:
                print(f"Stripe product already exists for {shoe.name}")

            if not shoe.stripe_price_id:
                print(f"Creating Stripe price for {shoe.name}...")
                # Create price
                price = stripe.Price.create(
                    unit_amount=int(shoe.price * 100),  # cents
                    currency="usd",  # or your currency
                    product=shoe.stripe_product_id,
                )
                shoe.stripe_price_id = price.id
            else:
                print(f"Stripe price already exists for {shoe.name}")

            shoe.save()
        print("Seeding to Stripe complete.")