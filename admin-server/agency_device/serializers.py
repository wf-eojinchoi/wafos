from rest_framework import serializers
from .models import AgencyDeviceInfo


class AgencyDeviceInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgencyDeviceInfo
        fields = '__all__'
        depth = 2
