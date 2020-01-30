from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    pay_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d %H:%M:%S')
    tran_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1


class PaymentAgencySerializer(serializers.ModelSerializer):
    pay_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d %H:%M:%S')
    tran_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1
