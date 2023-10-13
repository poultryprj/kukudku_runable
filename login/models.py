from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models




class LoginModel(models.Model):
    user_mobile_number = models.CharField(max_length=10, null=True)
    user_pin = models.CharField(max_length=12,null=True)
    

    def __str__(self):
        return self.user_mobile_number
    # def get_absolute_url(self):
    #     return reverse('admin:login', args=[self.username])
    
    

# def generate_api_key(user):
#     key, created = APIKey.objects.get_or_create(user=user)
#     if not created:
#         key.generate_key()
#         key.save()
#     return key
