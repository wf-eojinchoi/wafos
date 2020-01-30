from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from course_info.models import CourseInfo, StandardCourseInfo
from course_info.serializers import CourseInfoSerializer, StandardCourseInfoSerializer


class AgencyCourseList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = CourseInfoSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = CourseInfo.objects.filter(agency_device_id=self.kwargs.get('pk')).all().order_by('id')

        return queryset

    def get(self, request, *args, **kwargs):
        print(request.data, kwargs, args)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # return self.create(request, *args, **kwargs)
        resp = dict()
        resp['success'] = True
        agency_id = request.data.get('agency_id')
        agency_device_id = request.data.get('id')
        title = request.data.get('title')
        title_en = request.data.get('title_en')
        title_vn = request.data.get('title_vn')
        description = request.data.get('description')
        description_en = request.data.get('description_en')
        description_vn = request.data.get('description_vn')
        amount = request.data.get('amount')
        try:
            etc_count = CourseInfo.objects.filter(agency_id=agency_id, agency_device_id=agency_device_id, agency_device__etcDevice__type=6).all().count()
            print(etc_count)
            if etc_count == 4:
                resp['success'] = False
                resp['msg'] = '멀티자판기는 코스를 4개까지만 생성 가능합니다.'
                return Response(resp)

        except CourseInfo.DoesNotExist:
            pass

        agency_course_info = CourseInfo()
        agency_course_info.agency_id = agency_id
        agency_course_info.agency_device_id = agency_device_id
        agency_course_info.title = title
        agency_course_info.title_en = title_en
        agency_course_info.title_vn = title_vn
        agency_course_info.description = description
        agency_course_info.description_en = description_en
        agency_course_info.description_vn = description_vn
        agency_course_info.amount = amount
        agency_course_info.save()
        print(resp)
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = dict()
        resp['success'] = True
        print(request.data)
        agency_id = request.data.get('agency_id')
        agency_device_id = request.data.get('agency_device_id')
        title = request.data.get('title')
        title_en = request.data.get('title_en')
        title_vn = request.data.get('title_vn')
        description = request.data.get('description')
        description_en = request.data.get('description_en')
        description_vn = request.data.get('description_vn')
        amount = request.data.get('amount')
        agency_course_info = CourseInfo.objects.get(pk=request.data.get('id'))
        agency_course_info.title = title
        agency_course_info.title_en = title_en
        agency_course_info.title_vn = title_vn
        agency_course_info.description = description
        agency_course_info.description_en = description_en
        agency_course_info.description_vn = description_vn
        agency_course_info.amount = amount
        agency_course_info.save()
        return Response(resp)

    def delete(self, request, *args, **kwargs):
        resp = dict()
        try:
            resp['success'] = True
            course_info = CourseInfo.objects.get(pk=kwargs.get('pk'))
            course_info.delete()
        except:
            resp['success'] = False
        return Response(resp)


class StandardCourseList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = StandardCourseInfoSerializer

    def get_queryset(self, *args, **kwargs):
        type_ = self.request.query_params.get('type') #타입
        queryset = StandardCourseInfo.objects.filter(type=type_).all().order_by('id')
        sortby = self.request.query_params.get('sortby') #정렬
        descending = self.request.query_params.get('descending', None) # 내림차순
        order_by = None

        if sortby is not None:
            order_by = sortby

        if descending:
            order_by = '-' + sortby

        return queryset

    def get(self, request, *args, **kwargs):
        
        #get request.data.get('page'), request.data.get('sortby') , request.data.get('descending') 넘김
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # return self.create(request, *args, **kwargs)
        resp = dict()
        resp['success'] = True
        type = kwargs.get('pk')
        title = request.data.get('title')
        title_en = request.data.get('title_en')
        title_vn = request.data.get('title_vn')
        description = request.data.get('description')
        description_en = request.data.get('description_en')
        description_vn = request.data.get('description_vn')
        amount = request.data.get('amount')
        if type == 3:
            try:
                etc_count = StandardCourseInfo.objects.filter(type=6).all().count()
                print(etc_count)
                if etc_count == 4:
                    resp['success'] = False
                    resp['msg'] = '멀티자판기는 코스를 4개까지만 생성 가능합니다.'
                    return Response(resp)
            except StandardCourseInfo.DoesNotExist:
                pass
        course_info = StandardCourseInfo()
        if type == 0:
            course_info.type = type
        elif type == 1:
            course_info.type = 2
        elif type == 2:
            course_info.type = 3
        elif type == 3:
            course_info.type = 6
        course_info.title = title
        course_info.title_en = title_en
        course_info.title_vn = title_vn
        course_info.description = description
        course_info.description_en = description_en
        course_info.description_vn = description_vn
        course_info.amount = amount
        course_info.save()
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = dict()
        resp['success'] = True
        print(request.data)
        # type = request.data.get('type')
        title = request.data.get('title')
        title_en = request.data.get('title_en')
        title_vn = request.data.get('title_vn')
        description = request.data.get('description')
        description_en = request.data.get('description_en')
        description_vn = request.data.get('description_vn')
        amount = request.data.get('amount')
        course_info = StandardCourseInfo.objects.get(pk=request.data.get('id'))
        course_info.title = title
        course_info.title_en = title_en
        course_info.title_vn = title_vn
        course_info.description = description
        course_info.description_en = description_en
        course_info.description_vn = description_vn
        course_info.amount = amount
        course_info.save()
        return Response(resp)

    def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)
        resp = dict()
        try:
            resp['success'] = True
            course_info = StandardCourseInfo.objects.get(pk=kwargs.get('pk'))
            course_info.delete()
        except:
            resp['success'] = False
        return Response(resp)


class StandardCourseCopy(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        isSuccess = True
        print(request.data)
        try:
            device_info = request.data.get('device')
            etc_device_info = request.data.get('etcDevice')
            agency_info = request.data.get('agency')

            device_type = None
            if device_info is not None:
                device_type = device_info['type']
            if etc_device_info is not None:
                device_type = etc_device_info['type']

            standard_qs = StandardCourseInfo.objects.filter(type=device_type).all().order_by('id')

            # 기존 코스 삭제
            CourseInfo.objects.filter(agency_id=agency_info['id'], agency_device_id=request.data.get('id')).delete()
            # 표준 코스 복사
            for standard_ins in standard_qs:
                print(standard_ins.title)
                course_ins = CourseInfo()
                course_ins.agency_id = agency_info['id']
                course_ins.agency_device_id = request.data.get('id')
                course_ins.title = standard_ins.title
                course_ins.title_en = standard_ins.title_en
                course_ins.title_vn = standard_ins.title_vn
                course_ins.description = standard_ins.description
                course_ins.description_en = standard_ins.description_en
                course_ins.description_vn = standard_ins.description_vn
                course_ins.amount = standard_ins.amount
                course_ins.save()

            # StandardCourseInfo
            # CourseInfo()
        except:
            isSuccess = False

        resp['success'] = isSuccess

        return Response(resp)