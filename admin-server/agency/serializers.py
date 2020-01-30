from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Agency
from .models import Agency, AgencyPoint


class AgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Agency
        fields = '__all__'


class AgencyPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgencyPoint
        fields = '__all__'
        depth = 1

