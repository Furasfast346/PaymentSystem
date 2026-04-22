from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Discount(models.Model):
    name = models.CharField(max_length=150)
    percentage = models.IntegerField()
    stripe_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Tax(models.Model):
    name = models.CharField(max_length=150)
    percentage = models.IntegerField()
    stripe_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.ManyToManyField(Item, through='OrderItem')
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "Order " + str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
