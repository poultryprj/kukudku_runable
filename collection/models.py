from django.db import models
from enum import Enum
from django.contrib.postgres.fields import ArrayField
from users.models import userModel


def upload_to(instance, filename):
    return f'collection/{instance.shopId}/{filename}'


# Create your models here.
class collectionModel(models.Model):
    shopId = models.IntegerField(null=True)
    lati = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    longi = models.DecimalField(max_digits=10, decimal_places=5,null=True)
    paymentmethod = ArrayField(models.CharField(max_length=200, null=True))
    paidamount = models.CharField(max_length=50000,null=True)
    cheque_photo = models.FileField(blank=True, null=True, upload_to=f's3://kukudku/collection/cheques', max_length=2000)
    gpay_photo = models.FileField(blank=True, null=True, upload_to=f's3://kukudku/collection/gpay', max_length=2000)
    phonepe_photo = models.FileField(blank=True, null=True, upload_to=f's3://kukudku/collection/phonepe', max_length=2000)
    paytm_photo = models.FileField(blank=True, null=True, upload_to=f's3://kukudku/collection/paytm', max_length=2000)
    neft_imps_photo = models.FileField(blank=True, null=True, upload_to=f's3://kukudku/collection/neft_imps', max_length=2000)

    
    def __str__(self):
        return self.shopId
    

class collectionInfo(models.Model):
    collectionId = models.IntegerField(primary_key=True)
    collectionDate = models.DateField(auto_now=True)
    collectionTime = models.TimeField(auto_now=True)
    userId = models.ForeignKey(userModel, on_delete=models.SET_NULL, null=True)
    shopId = models.ForeignKey(collectionModel, on_delete=models.SET_NULL, null=True)
    collectionMode = models.CharField(max_length=10, null=True)
    collectionAmount = models.PositiveBigIntegerField()
    collectionVerified = models.CharField(max_length=30, null=True)	
    collectionConfimed = models.CharField(max_length=30, null=True)	
    accountCredited = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.collectionId
    
    
class collectionSkipped(models.Model):
    collectionId = models.ForeignKey(collectionInfo, on_delete=models.SET_NULL, null=True)
    collectionDate = models.DateField()
    collectionTime = models.TimeField()
    userId = models.ForeignKey(userModel, on_delete=models.CASCADE)
    shopId = models.ForeignKey(collectionModel, on_delete=models.SET_NULL, null=True)
    remark = models.TextField()
    confirmed = models.TextField()
    
    def __str__(self):
        return self.collectionId