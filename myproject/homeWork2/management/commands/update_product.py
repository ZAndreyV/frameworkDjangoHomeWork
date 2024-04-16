from django.core.management.base import BaseCommand
from homeWork3.models import Product


class Command(BaseCommand):
    help = 'Update product'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('amount', type=str, help='Product amount')
        parser.add_argument('price', type=str, help='Product price')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        amount = kwargs['amount']
        price = kwargs['price']
        product = Product.objects.filter(pk=pk).first()
        product.amount = amount
        product.price = price
        product.save()
        self.stdout.write(f'{product}')
