from django.core.management.base import BaseCommand
from homeWork2.models import Client


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        count = 0
        clients = Client.objects.all()
        if clients:
            for client in clients:
                self.stdout.write(f'Clint [id: {client.pk}]: {client}')
                count += 1
            self.stdout.write(f'Total: {count} clients')
        else:
            self.stdout.write('Clients record is empty...')