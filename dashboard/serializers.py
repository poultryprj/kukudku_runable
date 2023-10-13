from rest_framework import serializers
from dashboard.models import dashboardModel

class dashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=dashboardModel
        fields='__all__'    
