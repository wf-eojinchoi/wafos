from rest_framework import serializers
from .models import AgencyAccount
from django.contrib.auth.hashers import make_password


class AgencyAccountSerializer(serializers.ModelSerializer):

    def validate_pwd(self, value):
        return make_password(value)

    class Meta:
        model = AgencyAccount
        fields = '__all__'


class AgencyAccountDepthSerializer(serializers.ModelSerializer):

    pwd = serializers.CharField(write_only=True)
    api_seckey = serializers.CharField(write_only=True)

    class Meta:
        model = AgencyAccount
        fields = '__all__'
        depth = 1
