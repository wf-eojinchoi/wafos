from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.response import Response

from device_brand.models import Brand
from device_model.models import Model
from device_model.serializers import ModelSerializer


class ModelList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = ModelSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Model.objects.all().order_by('id')
        sortbyBrand = self.request.query_params.get('brand', None)
        print(sortbyBrand)
        if sortbyBrand is not None:
            try:
                brand_ins = Brand.objects.get(name=sortbyBrand)
                queryset = queryset.filter(brand_id=brand_ins.id)
            except Brand.DoesNotExist:
                pass
            print('###')
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        brand_name = request.data.get('brand_name', None)
        model_name = request.data.get('name', None)
        model_serial = request.data.get('serial', None)
        brand_ins = Brand.objects.get(name=brand_name)
        model_create = Model(name=model_name, serial=model_serial, brand_id=brand_ins.id).save()
        return Response({}, status=status.HTTP_201_CREATED)


class ModelDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = ModelSerializer

    def get_queryset(self):
        return Model.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)