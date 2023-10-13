from django.db import models

# Create your models here.
class dashboardModel(models.Model):
    CashierId = models.CharField(max_length=1000)
    RouteId = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.CashierId
