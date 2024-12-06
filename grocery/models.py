from django.db import models
from decimal import Decimal

class GroceryItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class GroceryTransaction(models.Model):
    item = models.ForeignKey(GroceryItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)  # To handle fractional quantities
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate total price based on price per kg
        self.total_price = self.item.price_per_kg * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item.name} - {self.quantity} units"