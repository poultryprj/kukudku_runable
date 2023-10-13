from django.db import models

# Create your models here.
#models.py
from django.db import models
# Create your models here.
class complaintModel(models.Model):
    #shopId = models.ForeignKey(cashiercollectionModel, on_delete=models.SET_NULL, null=True)
    shopname = models.CharField(max_length=1000,null=True)
    textfield = models.TextField(max_length=1000, null=True)
    file_upload = models.FileField(upload_to=f's3://kukudku/complaints/', null=True, blank=True)
    
    
    