from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.response import Response

from device_brand.models import Brand
from device_info.models import DeviceInfo
from device_info.serializers import DeviceSerializer
from device_model.models import Model


class DeviceList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = DeviceInfo.objects.all().order_by('id')

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        brand_name = request.data.get('brand_name')
        model_name = request.data.get('model_name')
        type = request.data.get('type')
        kg = request.data.get('kg')
        memo = request.data.get('memo')
        photo = request.data.get('photo')
        if brand_name is not None and model_name is not None:
            brand_ins = Brand.objects.get(name=brand_name)
            model_ins = Model.objects.get(name=model_name, brand_id=brand_ins.id)
            type_int = None
            if type == '세탁기':
                type_int = 0
            elif type == '건조기':
                type_int = 1
            DeviceInfo(brand_id=brand_ins.id, model_id=model_ins.id,
                       type=type_int, kg=kg, memo=memo, photo=photo).save()
            return Response({'success': True})
        else:
            return Response({ 'msg':'제조사, 모델 선택 후 다시 시도하세요.', 'success':False })
        # return self.create(request, *args, **kwargs)


class DeviceDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return DeviceInfo.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        # return self.partial_update(request, *args, **kwargs)
        brand_name = request.data.get('brand_name')
        model_name = request.data.get('model_name')
        type = request.data.get('type')
        kg = request.data.get('kg')
        memo = request.data.get('memo')
        photo = request.data.get('photo')
        id = request.data.get('id')
        if brand_name is not None and model_name is not None:
            brand_ins = Brand.objects.get(name=brand_name)
            model_ins = Model.objects.get(name=model_name, brand_id=brand_ins.id)
            type_int = None
            if type == '세탁기':
                type_int = 0
            elif type == '건조기':
                type_int = 1
            # DeviceInfo(brand_id=brand_ins.id, model_id=model_ins.id,
            #            type=type_int, kg=kg, memo=memo, photo=photo).upda()
            device_ins = DeviceInfo.objects.get(pk=id)
            device_ins.brand_id = brand_ins.id
            device_ins.model_id = model_ins.id
            device_ins.type = type_int
            device_ins.kg = kg
            device_ins.memo = memo
            device_ins.photo = photo
            device_ins.save()
            print('#1')
            return Response({ 'success':True })
        else:
            print('#2')
            return Response({ 'msg':'제조사, 모델 선택 후 다시 시도하세요.', 'success':False })

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)