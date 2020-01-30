from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import AdminAccount, VideoLinkInfo


class AdminAccountSerializer(serializers.ModelSerializer):
    reg_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d')

    def validate_pwd(self, value):
        return make_password(value)

    class Meta:
        model = AdminAccount
        fields = '__all__'


class VideoLinkInfoSerializer(serializers.ModelSerializer):
    reg_dttm = serializers.DateTimeField(
        read_only=True,
        format='%Y-%m-%d')

    class Meta:
        model = VideoLinkInfo
        fields = '__all__'