
from rest_framework import serializers
from complaint.models import complaintModel

class complaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= complaintModel
        fields='__all__'