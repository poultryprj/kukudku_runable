from django.db import models
from django.urls import reverse

# Create your models here.
class Routemodel(models.Model):
    RouteId = models.CharField(max_length=50, null=True)
    RouteName = models.CharField(max_length=50, null=True)
    RouteStartPoint = models.CharField(max_length=50, null=True)
    RouteEndPoint = models.CharField(max_length=50, null=True)
    RouteAreas = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.RouteId