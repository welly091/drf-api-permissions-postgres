from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('restaurant', 'title', 'price', 'description', 'created_at')
        model = Menu