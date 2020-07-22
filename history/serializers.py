from rest_framework import serializers
from .models import history

#music serializer
class historySerializer(serializers.ModelSerializer):
    class Meta:
        model = history
        fields = '__all__'