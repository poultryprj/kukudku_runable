from rest_framework import serializers
from collection.models import collectionModel ,  collectionInfo, collectionSkipped

class collectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=collectionModel, collectionInfo, collectionSkipped
        fields='__all__'    
