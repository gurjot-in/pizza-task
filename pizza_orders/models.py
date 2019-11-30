from django.db import models
from pizza_orders.constants import OrderStatus, PizzaFlavours, PizzaSizes

class Customer(models.Model):
    name = models.CharField(max_length=64 ,null=True, blank=True)
    phone_number = models.CharField(max_length=64, null=False, blank=False)
    address = models.CharField(max_length=64,  null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='order', null=False, blank=False, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=64,choices=OrderStatus.choices(), default = "Pending")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', null=True, blank=True, on_delete=models.CASCADE)
    pizza_flavour = models.CharField(max_length=64, choices=PizzaFlavours.choices(), null=False, blank=False)
    pizza_size = models.CharField(max_length=64, choices=PizzaSizes.choices(), null=False, blank=False)
    quantity = models.CharField(max_length=64, null=False, blank=False)
