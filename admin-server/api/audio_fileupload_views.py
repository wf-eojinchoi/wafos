from io import StringIO

from PIL import Image
from django.conf import settings
from django.core.files.base import ContentFile
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format='jpg'):
        resp = dict()
        # destination = open('/Users/Username/' + up_file.name, 'wb+')
        # for chunk in up_file.chunks():
        #     destination.write(chunk)
        #     destination.close()
        result = update_file(request)
        print(request.get_host(),result)
        if request.is_secure():
            protocol = 'https'
        else:
            protocol = 'http'
        resp['path'] = protocol + '://' + request.get_host() + result
        return Response(resp)


def update_file(request):
    import os
    print(request.data)
    print(request.FILES)
    atype = request.data.get('atype')[0]
    print(atype)
    data = {}
    # print("FILES %s" %(request.data['file'].name))

    if not 'file' in request.FILES:
        return Response({'msg': 'file missing.'}, status.HTTP_400_BAD_REQUEST)

    extension = request.data['file'].name.split('.')[-1]

    name = 'audio'
    if int(atype) == 0:
        name = 'byebye'
    elif int(atype) == 1:
        name = 'quiet'
    elif int(atype) == 2:
        name = 'pet'
    elif int(atype) == 3:
        name = 'siren'

    origin_name = '%s.%s' % (name, extension)
    path = "audio/"
    system_path = os.path.join(settings.MEDIA_ROOT, path)
    print("## path %s" % (settings.MEDIA_ROOT))
    try:
        if not os.path.exists(system_path):
            os.makedirs(system_path)
            print('makedirs')
    except OSError:
        print('OSError')

    path = system_path + origin_name
    print(path)
    if 'file' in request.FILES:
        file = request.FILES['file']
        filename = file._name

        fp = open(path, 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    return '/media/audio/' + origin_name

