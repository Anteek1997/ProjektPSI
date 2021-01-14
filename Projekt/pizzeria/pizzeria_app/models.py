from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name + ' ' + str(self.price) + 'zl'


class Sauce(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name + ' ' + str(self.price) + 'zl'


class Chef(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname


class Driver(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.surname


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname

class Order_Client(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.pizza.name + ' ' + self.client.name

class Order_Restaurant(models.Model):
    order_client = models.ForeignKey(Order_Client, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    prize_order = models.DecimalField(max_digits=5, decimal_places=2)
    date_realization = models.DateField()
