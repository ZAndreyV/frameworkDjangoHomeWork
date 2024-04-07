from datetime import datetime
from random import randint, choice
from django.core.management.base import BaseCommand
from homeWork2.models import Client, Product, Order



class Command(BaseCommand):
    help = "Create Orders (random)"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()

        for client in clients:
            order = Order(client=client,
                          total_price=0,
                          date=datetime.now())
            order.save()
            total_price = 0
            for i in range(randint(0, 5)):
                product = choice(products)
                order.product.add(product)
                order.save()
                total_price += product.price
            order.total_price = total_price
            order.save()
            print(order)

        self.stdout.write(f'All orders - created')
