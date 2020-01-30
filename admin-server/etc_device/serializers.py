from rest_framework import serializers
from .models import EtcDeviceInfo

class EtcDeviceSerializer(serializers.ModelSerializer):
    reg_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d')

    class Meta:
        model = EtcDeviceInfo
        fields = '__all__'

