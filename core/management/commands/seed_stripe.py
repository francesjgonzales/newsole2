import stripe
from django.core.management.base import BaseCommand
from core.models import Shoe  # adjust if your model name/path differs
from django.conf import settings

class Command(BaseCommand):
    help = "Create products and prices in Stripe based on Shoe model data"

    def handle(self, *args, **options):
        stripe.api_key = settings.STRIPE_API_KEY
        created = 0
        updated = 0

        for shoe in Shoe.objects.all():
            # Skip if already seeded
            if shoe.stripe_price_id:
                self.stdout.write(self.style.WARNING(f"⚠️ {shoe.name} already has a Stripe price ID. Skipping..."))
                continue

            # Step 1: Create Stripe Product
            product = stripe.Product.create(
                name=shoe.name,
                description=shoe.description or "",
            )

            # Step 2: Create Stripe Price
            price = stripe.Price.create(
                unit_amount=int(shoe.price * 100),  # Stripe expects cents
                currency="usd",
                product=product.id,
            )

            # Step 3: Save Stripe IDs to Django model
            shoe.stripe_price_id = price.id
            shoe.save()

            created += 1
            self.stdout.write(self.style.SUCCESS(f"✅ Created: {shoe.name} ({price.id})"))

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Done! {created} products created, {updated} updated."))
