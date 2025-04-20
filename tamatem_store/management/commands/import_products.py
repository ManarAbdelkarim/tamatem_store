import csv
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                products_created = 0
                for row in reader:
                    Product.objects.create(
                        title=row['title'],
                        description=row['description'],
                        price=row['price'],
                        location=row['location']
                    )
                    products_created += 1

                self.stdout.write(self.style.SUCCESS(
                    f"✅ Successfully imported {products_created} products."
                ))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("❌ CSV file not found."))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f"❌ Missing column in CSV: {e}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error: {e}"))
