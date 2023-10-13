from django.db import models
from shoplist.models import shoplistModel

# Create your models here.
class skipModel(models.Model):
    shopId = models.CharField(max_length=100,null=True)
    remark = models.CharField(max_length=1000,null=True)
    cashierId = models.CharField(max_length=10,null=True)
    routeId = models.CharField(max_length=500,null=True)
    
    def __str__(self):
        return self.shopId