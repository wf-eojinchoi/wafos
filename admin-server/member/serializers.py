from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    reg_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d %H:%M:%S')
    last_use_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Member
        fields = '__all__'
        depth = 1

