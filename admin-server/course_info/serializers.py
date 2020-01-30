from rest_framework import serializers
from .models import CourseInfo, StandardCourseInfo


class CourseInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseInfo
        fields = '__all__'
        depth = 2


class CourseInfoSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseInfo
        fields = '__all__'


class StandardCourseInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StandardCourseInfo
        fields = '__all__'
