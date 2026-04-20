from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, blank=True)
    price = models.IntegerField()
