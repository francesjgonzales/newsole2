from django.core.management.base import BaseCommand
from core.models import Shoe
from core.shoe_data import shoes  # assuming shoe_data.py is in the same directory  

class Command(BaseCommand):
    help = 'Seed the database with shoe products'

    def handle(self, *args, **kwargs):
        for data in shoes:
            shoe, created = Shoe.objects.get_or_create(
                product_code=data["product_code"],
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                    "image": data["image"],
                    "price": data["price"],
                    "categories": data["categories"],
                    "slug": data["slug"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {shoe.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Updated: {shoe.name}"))
