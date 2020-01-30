from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.response import Response

from etc_device.models import EtcDeviceInfo
from etc_device.serializers import EtcDeviceSerializer


class EtcDeviceList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = EtcDeviceSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = EtcDeviceInfo.objects.all().order_by('id')

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        name = request.data.get('name')
        memo = request.data.get('memo')
        photo = request.data.get('photo')
        try:
            p_type = request.data.get('type')
            type_int = None
            if p_type == '트롬스타일러':
                type_int = 2
            elif p_type == '운동화세탁기':
                type_int = 3
            elif p_type == '운동화건조기':
                type_int = 4
            elif p_type == '냉난방':
                type_int = 5
            elif p_type == '세탁용품':
                type_int = 6
            ed = EtcDeviceInfo(name=name, memo=memo, photo=photo, type=type_int).save()
            return Response({'success': True})
        except Exception as e:
            print('#', e)
            return Response({'success': False})


class EtcDeviceDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = EtcDeviceSerializer

    def get_queryset(self):
        return EtcDeviceInfo.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        print('#')
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)