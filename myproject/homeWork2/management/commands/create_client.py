from datetime import datetime
from django.core.management.base import BaseCommand
from homeWork3.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **options):
        # client = Client(
        #     name='Andrey',
        #     email='31m34@mail.com',
        #     phone_number='89059557545',
        #     address='Stroitelnay_9',
        #     date_reg=datetime.now()
        # )
        client = Client(
            name='Sara',
            email='123m34@mail.com',
            phone_number='89059557444',
            address='Stroitelnay_19',
            date_reg=datetime.now()
        )
        ...
        client.save()
        self.stdout.write(f'{client}')
