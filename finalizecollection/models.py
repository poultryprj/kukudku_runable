from django.db import models

# Create your models here.

class finalizecollectionModel(models.Model):
    cashierId = models.CharField(max_length=500, null=True)
    routeId = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.cashierId
    

