from rest_framework import serializers

from trans_info.models import TransInfo


class TransSerializer(serializers.ModelSerializer):
    reg_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d')

    class Meta:
        model = TransInfo
        fields = '__all__'

