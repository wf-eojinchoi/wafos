from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.response import Response

from user_history.models import UserHistory
from user_history.serializers import UserHistorySerializer


class UserHistoryList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = UserHistorySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = UserHistory.objects.all()

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserHistoryDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = UserHistorySerializer

    def get_queryset(self):
        return UserHistory.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)