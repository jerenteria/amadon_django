from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Order(models.Model):
    quantity=models.IntegerField()
    total_charge=models.IntegerField()
    items_ordered=models.ManyToManyField(Product, related_name="orders")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
