from django.db import models

# Create your models here.
class userModel(models.Model):
    userId = models.IntegerField(primary_key=True, unique=True)  
    userName = models.CharField(max_length=20, null=True)
    userMobileNo = models.PositiveBigIntegerField(null=True)
    userAlternateNo = models.IntegerField(null=True)
    userPassword = models.IntegerField(null=True)
    userLevel = models.CharField(max_length=20, null=True)
    
    
    def __str__(self):
        return self.userName
    
class userRoles(models.Model):
    userRoleId = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(userModel, on_delete=models.CASCADE)  
    roleId = models.IntegerField(null=True)
    roleActiveYN = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.userId
    
class Roles(models.Model):
    roleId = models.IntegerField(primary_key=True)
    roleName = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.roleId