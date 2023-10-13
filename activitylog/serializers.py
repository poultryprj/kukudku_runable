from rest_framework import serializers
from .models import activitylog

class activitylogSerializer(serializers.ModelSerializer):
    class Meta:
        model = activitylog
        fields = '__all__'
