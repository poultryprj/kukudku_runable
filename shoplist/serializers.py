from rest_framework import serializers
from shoplist.models import shoplistModel

class ShopListSerializer(serializers.ModelSerializer):
    """
    Serializer for the shopping list model
    """
    class Meta:
        model = shoplistModel
        fields = '__all__'
        #exclude = ('user',)