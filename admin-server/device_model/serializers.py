from rest_framework import serializers

from device_brand.models import Brand
from device_brand.serializers import BrandSerializer
from .models import Model

class ModelSerializer(serializers.ModelSerializer):
    #brand_id = serializers.SlugRelatedField(queryset=Brand.objects.all(), slug_field='id')

    class Meta:
        model = Model
        fields = '__all__'
        depth = 1

