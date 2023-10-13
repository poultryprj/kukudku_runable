from rest_framework import serializers
from finalizecollection.models import finalizecollectionModel


class finalizecollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = finalizecollectionModel
        fields ='__all__'