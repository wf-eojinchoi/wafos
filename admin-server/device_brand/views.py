from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.response import Response

from device_brand.models import Brand
from device_brand.serializers import BrandSerializer
from device_model.models import Model


class BrandList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Brand.objects.all().order_by('id')

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BrandDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brand.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):

        print(request.data, args, kwargs)
        brand_id = kwargs.get('pk', None)

        if brand_id is not None:
            try:
                model_ins = Model.objects.get(brand_id=brand_id)
                resp = dict()
                resp['error'] = True
                return Response(resp)
            except Model.DoesNotExist:
                return self.destroy(request, *args, **kwargs)


