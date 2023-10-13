from rest_framework import serializers
from users.models import userModel

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = '__all__'