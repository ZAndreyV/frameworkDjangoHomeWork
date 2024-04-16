from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.date_reg}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.amount} кг.'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order №: {self.id} from {self.date} client: {self.client.name}'
