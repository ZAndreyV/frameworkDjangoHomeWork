from datetime import datetime
from django.core.management.base import BaseCommand
from homeWork3.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **options):
        product = Product(
            name='Tomato',
            description='Lorem ipsum',
            price=140.25,
            amount=330,
            date=datetime.now()
        )
        # product = Product(
        #     name='Apple',
        #     description='Lorem ipsum',
        #     price=40.25,
        #     amount=630,
        #     date=datetime.now()
        # )
        product.save()
        self.stdout.write(f'{product}')
