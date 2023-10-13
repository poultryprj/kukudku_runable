from rest_framework import serializers
from shop.models import shopModel

class shopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shopModel
        fields = '__all__'