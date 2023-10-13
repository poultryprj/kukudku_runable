from rest_framework import serializers
from route.models import Routemodel

class routeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Routemodel
        fields='__all__'    