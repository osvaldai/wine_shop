# products/models.py

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Цена в евро")
    stock = models.PositiveIntegerField(default=100)  # Количество бутылок

    def __str__(self):
        return self.name
