from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from trans_info.models import TransInfo
from trans_info.serializers import TransSerializer


class TransList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = TransSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = TransInfo.objects.all().order_by('id')

        return queryset

    def get(self, request, *args, **kwargs):
        category = self.request.query_params.get('category', None)
        instance = TransInfo.objects.filter(category=category).all().order_by('id')
        serializer = TransSerializer(instance, many=True)
        obj = dict()
        obj = serializer.data
        return Response(obj)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TransDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = TransSerializer

    def get_queryset(self):
        return TransInfo.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TCopy(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        country = request.data.get('country')
        import json
        import os
        from django.conf import settings
        system_path = os.path.join(settings.MEDIA_ROOT, 'language')
        if country is not None:
            with open(system_path + '/%s.json' % country) as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    sub_data = value
                    if key == 'app' or key == 'payment' or key == 'home' or key == 'init' or key == 'build'\
                            or key == 'menu':
                        for skey, svalue in sub_data.items():
                            trans = TransInfo()
                            trans.category = key
                            trans.keyword = skey
                            if country == 'kr':
                                trans.kr = svalue
                            elif country == 'en':
                                trans.en = svalue
                            elif country == 'vn':
                                trans.vn = svalue
                            trans.save()
                    else:

                        for skey, svalue in sub_data.items():
                            # print(svalue)
                            # resp[key][skey] = dict()
                            resp['%s-%s'%(key, skey)] = dict()
                            for innerKey, innerValue in svalue.items():
                                resp['%s-%s' % (key, skey)][innerKey] = innerValue
                                trans = TransInfo()
                                trans.category = '%s-%s' % (key, skey)
                                trans.keyword = innerKey
                                if country == 'kr':
                                    trans.kr = innerValue
                                elif country == 'en':
                                    trans.en = innerValue
                                elif country == 'vn':
                                    trans.vn = innerValue
                                trans.save()
                                # print(innerKey, innerValue)

        return Response(resp)
