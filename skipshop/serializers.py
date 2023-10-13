from rest_framework import serializers
from skipshop.models import skipModel

class skipSerializer(serializers.ModelSerializer):
    class Meta:
        model=skipModel
        fields='__all__'    
