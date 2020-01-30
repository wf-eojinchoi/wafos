from rest_framework import serializers
from .models import AlertInfo


class AlertInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlertInfo
        fields = '__all__'
        depth = 1
