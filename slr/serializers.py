# # slr/serializers.py
# from rest_framework import serializers
# from .models import Shop,Route

# class ShopSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shop,Route
#         fields = '__all__'


# serializers.py

from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'outstanding_amount')  # Include the 'outstanding_amount' field
