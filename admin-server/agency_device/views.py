from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from agency_device.models import AgencyDeviceInfo
from agency_device.serializers import AgencyDeviceInfoSerializer


class AgencyDeviceInfoList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyDeviceInfoSerializer

    def get_queryset(self, *args, **kwargs):
        agency_id = self.request.data.get('id')
        queryset = AgencyDeviceInfo.objects.filter(
            agency_id=self.kwargs['pk']).order_by('controller_id')

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # return self.create(request, *args, **kwargs)
        resp = dict()
        print(request.data)
        resp['success'] = True
        agency = request.data.get('agency')
        device = request.data.get('device')
        controller_id = request.data.get('controller_id')
        used = request.data.get('used')
        agency_device_info = AgencyDeviceInfo()
        agency_device_info.controller_id = controller_id
        agency_device_info.current_coin = agency['current_coin']
        agency_device_info.min_coin = agency['min_coin']
        agency_device_info.max_coin = agency['max_coin']
        agency_device_info.min_etc_coin = agency['min_etc_coin']
        agency_device_info.capacity = agency['capacity']
        if device['type'] < 2:
            agency_device_info.device_id = device['id']
        else:
            agency_device_info.etcDevice_id = device['id']
        agency_device_info.agency_id = request.data.get('id')
        agency_device_info.used = True if used == '사용' else False
        agency_device_info.save()
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = dict()
        print(request.data)
        resp['success'] = True
        agency = request.data.get('agency')
        device = request.data.get('device')
        controller_id = request.data.get('controller_id')
        used = request.data.get('used')
        adInfo_id = request.data.get('adInfo_id')
        agency_device_info = AgencyDeviceInfo.objects.get(pk=adInfo_id)
        if controller_id is not None:
            agency_device_info.controller_id = controller_id
        agency_device_info.current_coin = agency['current_coin']
        agency_device_info.min_coin = agency['min_coin']
        agency_device_info.max_coin = agency['max_coin']
        agency_device_info.min_etc_coin = agency['min_etc_coin']
        agency_device_info.capacity = agency['capacity']
        if device['type'] < 2:
            agency_device_info.device_id = device['id']
        else:
            agency_device_info.etcDevice_id = device['id']
        agency_device_info.used = True if used == '사용' else False
        agency_device_info.save()
        return Response(resp)

    def delete(self, request, *args, **kwargs):
        resp = dict()
        print(request.data, kwargs, args)
        # return self.destroy(request, *args, **kwargs)
        return Response(resp)


class AgencyDeviceInfoDelete(
        mixins.DestroyModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyDeviceInfoSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = AgencyDeviceInfo.objects.all().order_by('controller_id')

        return queryset

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AgencyDeviceInfoAllList(
        mixins.ListModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyDeviceInfoSerializer

    def get_queryset(self, *args, **kwargs):
        dev_type = self.request.query_params.get('type', None)
        queryset = AgencyDeviceInfo.objects.all().order_by('controller_id')
        if dev_type:
            queryset = queryset.filter(device__type=dev_type)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AgencyDeviceInfoDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyDeviceInfoSerializer

    def get_queryset(self):
        return AgencyDeviceInfo.objects.all().order_by('controller_id')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ControllerIdList(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        print(request.data, args, kwargs)
        agency_id = kwargs.get('pk', None)
        controller_id = request.data.get('controller_id')
        if agency_id is not None:
            compare_list = []
            try:
                ad_info_qs = AgencyDeviceInfo.objects.filter(
                    agency_id=agency_id).all()
                for ad_ins in ad_info_qs:
                    if controller_id is not None and controller_id == ad_ins.controller_id:
                        print('inner:', ad_ins.controller_id)
                        pass
                    else:
                        print('outer:', ad_ins.controller_id)
                        compare_list.append(ad_ins.controller_id)
            except AgencyDeviceInfo.DoesNotExist:
                print('###')
                pass
            id_list = []
            for ctrl_id in range(1, 21):
                if ctrl_id not in compare_list:
                    id_list.append(ctrl_id)
            resp['id_list'] = id_list
            resp['success'] = True
        else:
            resp['success'] = False
            resp['msg'] = '가맹점 ID 정보 없음'
        return Response(resp)


class AllowControlIdList(APIView):
    def get(self, request, *args, **kwargs):
        resp = dict()
        print(request.data, args, kwargs)
        agency_id = kwargs.get('agency', None)
        if agency_id is not None:
            id_list = []
            try:
                ad_info_qs = AgencyDeviceInfo.objects.filter(
                    agency_id=agency_id).all().order_by('controller_id')
                for ad_ins in ad_info_qs:
                    id_list.append(ad_ins.controller_id)
            except AgencyDeviceInfo.DoesNotExist:
                print('###')
                pass
            resp['id_list'] = id_list
            resp['success'] = True
        else:
            resp['success'] = False
            resp['msg'] = '가맹점 ID 정보 없음'
        return Response(resp)