from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView

from agency.models import Agency, AgencyPoint
from agency.serializers import AgencySerializer, AgencyPointSerializer
from agency_account.models import AgencyAccount
from agency_device.models import AgencyDeviceInfo
from alert_info.models import AlertInfo


class AgencyList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Agency.objects.all().order_by('reg_dttm')
        location = self.request.query_params.get('location') # 지역검색
        agency_name = self.request.query_params.get('name') # 지점검색
        sortby = self.request.query_params.get('sortby') #정렬
        descending = self.request.query_params.get('descending', None) # 내림차순
        #지역검색
        if location is not None:
            if location == '전체':
                pass
            else:
                queryset = queryset.filter(addr1__contains=location)
        #지점검색
        if agency_name is not None:
            queryset = queryset.filter(agency_name__contains=agency_name)
        order_by = None
        if sortby is not None:
            order_by = sortby

        if descending:
            order_by = '-' + sortby

        print('order_by :{} , descending :{}',order_by, descending)
        return queryset.order_by(order_by) if order_by is not None else queryset.order_by('agency_name')

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs) #page 변수가 넘어갔을듯..

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print('가맹점 생성 -> ', serializer.data)
        headers = self.get_success_headers(serializer.data)
        # 포인트 레코드 생성
        agency_id = serializer.data['id']
        agency_code = serializer.data['agency_code']
        # api_secretkey 새성하기
        import hashlib
        hashkey = hashlib.sha1()
        hashkey.update(agency_code.encode())
        #
        try:
            AgencyPoint.objects.get(agency_id=agency_id)
        except AgencyPoint.DoesNotExist:
            AgencyPoint(agency_id=agency_id).save()
        # 가맹점 계정 생성
        try:
            AgencyAccount.objects.get(agency_id=agency_id)
        except AgencyAccount.DoesNotExist:
            AgencyAccount(agency_id=agency_id, login_id=agency_code, pwd=make_password(
                '0000'), api_seckey=hashkey.hexdigest()).save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AgencyDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

    # permission_classes = (IsAuthenticated, )
    serializer_class = AgencySerializer

    def get_queryset(self):
        return Agency.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data
        print(obj)
        agency_acc = AgencyAccount.objects.get(
            agency_id=obj['id'], login_id=obj['agency_code'])
        obj['api_seckey'] = agency_acc.api_seckey

        print(obj['api_seckey'])

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AgencyPointInfo(
        mixins.UpdateModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyPointSerializer

    def get_queryset(self):
        return AgencyPoint.objects.all()

    def get(self, request, *args, **kwargs):
        instance = AgencyPoint.objects.get(agency_id=kwargs['pk'])
        serializer = AgencyPointSerializer(instance)
        obj = serializer.data
        print(kwargs['pk'])
        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AgencyListAll(APIView):
    def get(self, request, *args, **kwargs):
        obj = dict()
        obj['success'] = True
        obj['results'] = AgencySerializer(Agency.objects.all(), many=True).data
        return Response(obj)


# 경고방송 등록API 
class AgencyAlertRegist(APIView):
    def post(self, request, *args, **kwargs):
        obj = dict()
        try:
            # (0, '퇴출요청'),   >> args 에 URL 삽입
            # (1, '장난금지'),   >> args 에 URL 삽입
            # (2, '동물퇴출'),   >> args 에 URL 삽입
            # (3, '사이렌'),   >> args 에 URL 삽입
            # (4, '냉난방기 켜기'),  >> 디바이스리스트에서 ctrl 리스트 검색해서 키오스크에 전달
            # (5, '장비전원 재시작'),
            # (6, 'PC재부팅')
            # (7, '코인신호보내기') >> args 에  { ctrl_id, coin } 삽입
            # (8, '업데이트 진행') >> args 에 패쓰
            print(request.data)
            cmd = request.data.get('cmd')
            ctrl_id = request.data.get('ctrl_id')
            coin = request.data.get('coin')
            onoff = request.data.get('onoff')
            agency_id = request.data.get('agency_id')
            alert_ins = AlertInfo()
            alert_ins.agency_id = agency_id
            alert_ins.cmd = cmd
            path = None
            print('cmd :{} , agency_id:{}'.format(cmd,agency_id))
            print('ctrl_id :{} , ctrl_id:{} , onoff:{}'.format(ctrl_id,ctrl_id,onoff))
            print('AlertInfo :{} , alert_ins.agency_id:{}, alert_ins.cmd:{} '.format(alert_ins,alert_ins.agency_id,alert_ins.cmd))
            from washfriends.settings import WF_HOST_DOMAIN
            host_domain = WF_HOST_DOMAIN
            arg_dict = dict()
            if int(cmd) == 0:  # 호스트 도메인 붙여야함
                path = '/media/audio/byebye.wav'
                print('path: {}'.format(path))
            elif int(cmd) == 1:  # 호스트 도메인 붙여야함
                path = '/media/audio/quiet.wav'
                print('path: {}'.format(path))
            elif int(cmd) == 2:  # 호스트 도메인 붙여야함
                path = '/media/audio/pet.wav'
                print('path: {}'.format(path))
            elif int(cmd) == 3:  # 호스트 도메인 붙여야함
                path = '/media/audio/siren.wav'
                print('path: {}'.format(path))
            elif int(cmd) == 10:  # 호스트 도메인 붙여야함
                path = '/media/audio/bayernAlert.wav'
                print('path: {}'.format(path))
            elif int(cmd) == 4:  # 호스트 도메인 붙여야함
                try:
                    device = AgencyDeviceInfo.objects.filter(
                        agency_id=agency_id, etcDevice__type=5).latest('controller_id')
                    arg_dict['ctrl_id'] = device.controller_id
                    arg_dict['coin'] = 1
                    path = arg_dict
                except AgencyDeviceInfo.DoesNotExist:
                    path = None
                    obj['success'] = False
                    obj['msg'] = '냉난방기가 설치되어 있지 않아 이용 할 수 없습니다.'
                    return Response(obj)
            elif int(cmd) == 5:
                arg_dict['ctrl_id'] = ctrl_id
                arg_dict['onoff'] = onoff
                path = arg_dict
            elif int(cmd) == 7:
                arg_dict['ctrl_id'] = ctrl_id
                arg_dict['coin'] = coin
                path = arg_dict
            # 업데이트 신호 처리
            elif int(cmd) == 8:
                path = makeUpdatePath()
            # 업데이트 신호

            else:
                path = None


            print('if문 다건너옴')
            print('path : {}'.format(path))
            alert_ins.args = path
            print('args : {}'.format(alert_ins.args))
            alert_ins.flag = False
            print('flag : {}'.format(alert_ins.flag))

            alert_ins.save() # wafoss db의 alert_info에 insert하는 녀석. db에 추가하면, agent에서 일정시간마다 db를 조회해서 실행시킴.

            # 저장내용은 실행시킬녀석이 어디에있는지 알려주는 path, 그리고 아직실행전임을 알려주는 False를 추가한다.
            # 그럼 agent단에서는  path를 읽어서 위치를 찾고 실행이 완료되면, args를 true로 바꿔주는 작업을 하겠네??

            obj['success'] = True
            print('obj[success] :{}'.format(obj['success']))
        except:
            obj['success'] = False
            print('except에 걸림')
        return Response(obj)


class AgencyUpdateAll(APIView):
    def get(self, request, *args, **kwargs):
        obj = dict()
        try:
            agency_qs = Agency.objects.all()
            for agency in agency_qs:
                alert_ins = AlertInfo() 
                alert_ins.agency_id = agency.id
                alert_ins.cmd = 8
                alert_ins.args = makeUpdatePath()
                alert_ins.flag = False
                alert_ins.save()
            obj['success'] = True
        except:
            obj['success'] = False

        return Response(obj)

# 업데이트 하고자하는 파일 리스트업
def makeUpdatePath():
    import os
    from django.conf import settings
    system_path = os.path.join(settings.MEDIA_ROOT, 'update') # ~/update
    
    #나는 여기 경로가궁금하다.. 뒤져봐도 잘모르겠다.
    print("system_path : {}".format(system_path))

    files = os.listdir(system_path) # ~/update 폴더에서 파일리스트를 담는다.
    if not files:
        return '' # 읽을 파일이 없다면 끝낸다.
    files.sort(reverse=True) # 읽을 파일이 있따면 정렬한다.

    path = os.path.join(settings.MEDIA_URL, 'update')

    #나는 여기 경로가궁금하다.. 뒤져봐도 잘모르겠다.
    print("path : {}".format(path))

    path = os.path.join(path, files[0])

    return path
