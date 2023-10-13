from rest_framework import serializers
from login.models import LoginModel

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoginModel
        fields='__all__'    
