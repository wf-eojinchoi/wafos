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
        up_file = request.data['file']
        print('##',request.FILES)
        # destination = open('/Users/Username/' + up_file.name, 'wb+')
        # for chunk in up_file.chunks():
        #     destination.write(chunk)
        #     destination.close()
        result = update_image(request)
        print(request.get_host(),result)
        if request.is_secure():
            protocol = 'https'
        else:
            protocol = 'http'
        resp = dict()
        resp['image_url'] = protocol + '://' + request.get_host() + result
        return Response(resp)


def update_image(request, member_index='board'):
    import os
    from PIL import Image as PILImg
    import datetime
    from PIL import ImageEnhance as PILImageEnhance

    data = {}
    print("FILES %s" %(request.data['file'].name))

    if not 'file' in request.FILES:
        return Response({'msg': 'Photo missing.'}, status.HTTP_400_BAD_REQUEST)
    try:
        im = Image.open(request.data['file'])
    except IOError:
        return Response({'msg': 'Bad image.'}, status.HTTP_400_BAD_REQUEST)

    extension = request.data['file'].name.split('.')[-1]

    origin_name = datetime.datetime.now().strftime(member_index+"_%Y%m%d_%H%M%S." + extension)

    path = "board/" + datetime.datetime.now().strftime("%Y%m%d") + "/"
    system_path = os.path.join(settings.MEDIA_ROOT, path)
    print("## path %s" % (settings.MEDIA_ROOT))
    try:
        if not os.path.exists(system_path):
            os.makedirs(system_path)
            print('makedirs')
    except OSError:
        print('OSError')

    path = system_path + origin_name

    imageType = 'JPEG'
    if extension == 'jpg':
        imageType = 'JPEG'
    im.save(path, imageType)
    # system_path = os.path.join(settings.MEDIA_ROOT, path)
    # original_file = os.path.join(settings.MEDIA_ROOT, path)
    #
    # if os.path.isfile(original_file):
    #     os.remove(original_file)
    #
    #
    # with open(original_file, 'wb+') as f:
    #     f.write(request.data['file'].read())
    # resize image
    # image = PILImg.open(origin_form)
    # image = image.resize((150, 150), PILImg.ANTIALIAS)
    # # sharpness image
    # image = PILImageEnhance.Sharpness(image)
    # image = image.enhance(1.3)

    return '/media/board/' + datetime.datetime.now().strftime("%Y%m%d/") + origin_name


def resize_image(im, edge):
    (width, height) = im.size
    (width, height) = scale_dimension(width, height, long_edge=edge)
    content = StringIO()
    im.resize((width, height), Image.ANTIALIAS).save(fp=content, format='JPEG', dpi=[72, 72])
    return ContentFile(content.getvalue())

def scale_dimension(width, height, long_edge):
    if width > height:
        ratio = long_edge * 1. / width
    else:
        ratio = long_edge * 1. / height
    return int(width * ratio), int(height * ratio)