from django.db import models


# Create your models here.
class shopModel(models.Model):
    shopCode = models.CharField(null=True)
    shopName = models.CharField(max_length=100, null=True)
    shopArea = models.CharField(max_length=100, null=True)
    shopLatitude = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    shopLongitude = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    shopAddress = models.CharField(max_length=100,null=True)
    shopPincode = models.IntegerField(null=True)
    shopDistance = models.IntegerField(null=True)
    shopMobileNo = models.CharField(null=True)
    shopAlternateNo = models.CharField(null=True)
    shopOwnerId = models.BigIntegerField(null=True)
    shopType = models.CharField(max_length=20,null=True)
    shopStatus = models.CharField(max_length=15,null=True)
    shopFlexibleRate = models.CharField(max_length=5,null=True)
    
    def __str__(self):
        return self.shopCode
    
class shopOwners(models.Model):
    ownerName = models.CharField(max_length=100,null=True)
    ownerContactNo = models.CharField(max_length=10, null=True)
    ownerAlternateNo = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.ownerName
    
class shopRoutes(models.Model):
    routeId = models.CharField(max_length=10,null=True)
    shopId = models.CharField(max_length=10,null=True)
    shopOrder = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.routeId              
    
    
class shopBalances(models.Model):
    shopId = models.CharField(max_length=500, null=True)
    shopBalance = models.BigIntegerField(null=True)
    
    
    def __str__(self):
        return self.shopId