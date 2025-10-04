import csv
from django.core.management.base import BaseCommand
from core.models import Shoe

class Command(BaseCommand):
    help = "Update Stripe Price IDs in Shoe model using data from products.csv"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the Stripe products CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        updated = 0
        not_found = []

        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name'].strip()
                    price_id = row['Price ID'].strip()

                    try:
                        shoe = Shoe.objects.get(name=name)
                        shoe.stripe_price_id = price_id
                        shoe.save()
                        updated += 1
                        self.stdout.write(self.style.SUCCESS(f"Updated: {name} -> {price_id}"))
                    except Shoe.DoesNotExist:
                        not_found.append(name)

            self.stdout.write(self.style.SUCCESS(f"\n✅ Done! {updated} shoes updated."))

            if not_found:
                self.stdout.write(self.style.WARNING("\n⚠️ Not found in database:"))
                for name in not_found:
                    self.stdout.write(f" - {name}")

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"❌ File not found: {csv_file}"))
