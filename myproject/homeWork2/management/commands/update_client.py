from django.core.management.base import BaseCommand
from homeWork3.models import Client


class Command(BaseCommand):
    help = 'Update client'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('phone_number', type=str, help='Client phone_number')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']
        phone_number = kwargs['phone_number']
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.phone_number = phone_number
        client.save()
        self.stdout.write(f'{client}')
