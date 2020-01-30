from rest_framework import serializers
from .models import DeviceInfo

class DeviceSerializer(serializers.ModelSerializer):
    reg_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d')

    class Meta:
        model = DeviceInfo
        fields = '__all__'
        depth = 1

