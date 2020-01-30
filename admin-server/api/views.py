from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_account.models import VideoLinkInfo
from admin_account.serializers import VideoLinkInfoSerializer
from member.models import Member

class TubeLink(APIView):
    def get(self, request, *args, **kwargs):
        resp = dict()
        try:
            v = VideoLinkInfo.objects.latest('upd_dttm')
        except VideoLinkInfo.DoesNotExist:
            v = VideoLinkInfo(link_path=None).save()
        resp = VideoLinkInfoSerializer(v).data
        return Response(resp)

    def post(self, request, *args, **kwargs):
        print(request.data)
        r = dict()
        try:
            v = VideoLinkInfo.objects.latest('upd_dttm')
            v.link_path = request.data.get('link_path')
            v.save()
            r['success'] = True
        except:
            r['success'] = False
        return Response(r)
