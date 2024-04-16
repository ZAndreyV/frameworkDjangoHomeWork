from decimal import Decimal
from datetime import timedelta
from random import randint, uniform, choice

from django.utils.timezone import now
from django.core.management.base import BaseCommand

from homeWork3.models import Client, Product, Order


class DBDataError(Exception):
    pass


class Command(BaseCommand):
    help = (f'Генерация записей Клиента, Товара и Заказа с последующим сохранением в БД. '
            f'Примеры использования: '
            f'"python manage.py generate_fake_data 10 20 5", '
            f'"python manage.py generate_fake_data 0 0 5". '
            )

    def add_arguments(self, parser):
        parser.add_argument('clients_qty', type=int, help='Количество клиентов')
        parser.add_argument('products_qty', type=int, help='Количество товаров')
        parser.add_argument('orders_qty', type=int, help='Количество заказов')

    def handle(self, *args, **options):
        clients_qty = options.get('clients_qty')
        products_qty = options.get('products_qty')
        orders_qty = options.get('orders_qty')

        # Определим стартовые номера счетчиков во избежание повторов
        clients_start_counter = len(Client.objects.all())
        products_start_counter = len(Product.objects.all())
        orders_start_counter = len(Order.objects.all())

        # Создание Клиентов
        for i in range(clients_qty + 1, clients_start_counter + clients_qty + 1):
            client = Client(
                name=f'Client_{i}',
                email=f'mail_{i}@mail.ml',
                phone_number=f"+7{''.join([str(randint(0, 9)) for _ in range(10)])}",
                address=f'Строительная {i}',
                date_reg=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59)
                ),

            )
            self.stdout.write(f'{client}')
            client.save()

        # Создание Товаров
        for i in range(products_start_counter + 1, products_start_counter + products_qty + 1):
            product = Product(
                name=f'Product_{i}_Title',
                description=f'Product_{i}_Description',
                price=round(uniform(1, 10_000), 2),
                amount=randint(1, 100),
                date=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59),
                ),
            )
            product.save()

        # Создание Заказов
        # Проверка на существующие записи Клиентов и Товаров
        client = Client.objects.all()
        if len(client) == 0:
            raise DBDataError('В БД отсутствуют Клиенты')
        products = Product.objects.all()
        if len(products) == 0:
            raise DBDataError('В БД отсутствуют Товары')

        for i in range(orders_start_counter + 1, orders_start_counter + orders_qty + 1):
            order = Order(
                client=choice(client),
                total_price=0,
                date=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59),
                ),
            )
            order.save()
            # Наполнение заказа товарами и расчет общей стоимости
            products_to_order = [choice(products) for _ in range(randint(1, 5))]
            order.product.set(products_to_order)
            order.total = sum([Decimal(i.price) for i in order.product.all()])
            order.save()

        self.stdout.write(
            f'БД успешно заполнена клиентами: {clients_qty}, товарами: {products_qty}, заказами: {orders_qty}')