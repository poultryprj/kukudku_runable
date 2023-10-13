from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    outstanding_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
