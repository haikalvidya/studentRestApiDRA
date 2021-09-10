from rest_framework import serializers
from .models import CRUDApi

class CRUDApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRUDApi
        fields = '__all__'