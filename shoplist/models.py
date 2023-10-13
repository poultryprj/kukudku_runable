from django.db import models

# Create your models here.
class shoplistModel(models.Model):
    shopCode = models.CharField(max_length=500, null=True)
    shopname = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.shopname
    
    
    
   