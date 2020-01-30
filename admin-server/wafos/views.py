import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_account.models import VideoLinkInfo
from admin_account.serializers import VideoLinkInfoSerializer
from agency.models import AgencyPoint
from agency.serializers import AgencyPointSerializer
from alert_info.models import AlertInfo
from alert_info.serializers import AlertInfoSerializer
from member.models import Member, LoginInfo
from member.serializers import MemberSerializer
from course_info.models import CourseInfo
from course_info.serializers import CourseInfoSimpleSerializer
from agency_device.models import AgencyDeviceInfo
from agency_device.serializers import AgencyDeviceInfoSerializer
from agency_account.models import AgencyAccount
from agency_account.serializers import AgencyAccountDepthSerializer
from payment.models import Payment
from payment.serializers import PaymentAgencySerializer
from .permissions import agency_required


class MemberLogin(
        generics.GenericAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.get(tel=self.request.data.get('tel'))
        # return Member.objects.all()

    @agency_required
    def post(self, request, *args, **kwargs):
        resp = dict()
        try:
            mem_ins = Member.objects.get(tel=request.data.get('tel'),
                                         agency=self.agency)

            if request.data.get('pwd', '') == mem_ins.pwd:
                resp['point'] = mem_ins.point
                resp['money'] = mem_ins.money
                resp['pwd'] = mem_ins.pwd
                resp['id'] = mem_ins.id

                # 로그인 정보 저장
                LoginInfo(tel=mem_ins.tel, agency=self.agency, point=mem_ins.point, money=mem_ins.money).save()
                return Response(resp)
        except Member.DoesNotExist:
            return Response(resp, status=status.HTTP_403_FORBIDDEN)

        return Response([], status=status.HTTP_401_UNAUTHORIZED)


class MemberSignUp(APIView):
    @agency_required
    def post(self, request, *args, **kwargs):
        tel = request.data.get('tel')
        pwd = request.data.get('pwd')

        try:
            Member.objects.get(tel=tel, agency=self.agency)
            return Response({'detail': 'exists'}, status=status.HTTP_403_FORBIDDEN)
        except Member.DoesNotExist:
            member = Member(tel=tel, agency=self.agency, pwd=pwd)
            # member.point = signUpPoint(agency_id=self.agency.id)
            member.save()

        return Response([])


def signUpPoint(agency_id, pay_type):
    # ['월', '화', '수', '목', '금', '토', '일']
    today = datetime.datetime.today()
    week = today.weekday()

    agency_pt_ins = AgencyPoint.objects.get(agency_id=agency_id)
    ret_point = 0
    isEvent = False
    if agency_pt_ins.evt_st_date is not None and agency_pt_ins.evt_et_date is not None:
        if today.date() >= agency_pt_ins.evt_st_date and today.date() <= agency_pt_ins.evt_et_date:
            if week < 5:
                ret_point = agency_pt_ins.evt_day_new
            else:
                ret_point = agency_pt_ins.evt_weekend_new
            isEvent = True
        else:
            if pay_type == 0:
                if week < 5:
                    ret_point = agency_pt_ins.def_day_new
                else:
                    ret_point = agency_pt_ins.def_weekend_new
            elif pay_type == 2:
                if week < 5:
                    ret_point = agency_pt_ins.def_card_day_new
                else:
                    ret_point = agency_pt_ins.def_card_weekend_new
    else:
        if pay_type == 0:
            if week < 5:
                ret_point = agency_pt_ins.def_day_new
            else:
                ret_point = agency_pt_ins.def_weekend_new
        elif pay_type == 2:
            if week < 5:
                ret_point = agency_pt_ins.def_card_day_new
            else:
                ret_point = agency_pt_ins.def_card_weekend_new

    return ret_point, isEvent


class AgencyInitCheck(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        kid = request.data.get('kid', None)
        seckey = request.data.get('seckey', None)

        if not (kid and seckey):
            return Response(status=status.HTTP_403_FORBIDDEN)

        agency = None
        try:
            agency = AgencyAccount.objects.get(login_id=kid, api_seckey=seckey)
        except AgencyAccount.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if agency.agency.ip_addr == '':
            agency.agency.ip_addr = request.META.get('HTTP_REFERER', '')
            agency.agency.save()

        return Response()


class AgencyAccountDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

    serializer_class = AgencyAccountDepthSerializer
    lookup_field = 'login_id'

    def get_queryset(self):
        return AgencyAccount.objects.all()

    @agency_required
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AgencyDeviceInfoAllList(
        mixins.ListModelMixin,
        generics.GenericAPIView):

    serializer_class = AgencyDeviceInfoSerializer

    def get_queryset(self, *args, **kwargs):
        dev_type = self.request.query_params.get('type', None)
        queryset = AgencyDeviceInfo.objects.filter(
            agency=self.agency).order_by('controller_id')
        if dev_type and dev_type.isdigit():
            dev_type = int(dev_type)
            if dev_type < 2:
                queryset = queryset.filter(device__type=dev_type)
            else:
                queryset = queryset.filter(etcDevice__type=dev_type)

        return queryset

    @agency_required
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AgencyCourseList(
        mixins.ListModelMixin,
        generics.GenericAPIView):

    serializer_class = CourseInfoSimpleSerializer

    def get_queryset(self, *args, **kwargs):
        device_id = self.request.query_params.get('device_id', None)
        queryset = CourseInfo.objects.filter(
            agency=self.agency).order_by('reg_dttm')
        if device_id and device_id.isdigit():
            device_id = int(device_id)
            queryset = queryset.filter(agency_device__id=device_id)

        return queryset

    @agency_required
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# 선택 후 결제들어갈때
class AgencyPayment(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        agency_id = request.data.get('agency_id')
        member_id = request.data.get('member_id')
        # 처리 금액
        amount = request.data.get('amount')
        # 사용 포인트 :
        use_point = request.data.get('use_point', 0)
        # pay_type
        # (0, '현금'),
        # (1, '포인트'),
        # (2, '카드'),
        # (3, '적립금 사용')
        pay_type = request.data.get('pay_type')
        # device type
        # (0, '세탁기'),
        # (1, '건조기'),
        # (2, '트롬스타일러'),
        # (3, '운동화세탁기'),
        # (4, '운동화건조기'),
        # (5, '냉난방'),
        # (6, '세탁용품')
        device_type = request.data.get('device_type')

        # 결제 타입 빼먹으면
        if pay_type is None:
            resp['success'] = False
            resp['msg'] = '결제 타입 선택 안함'
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)

        pay_type = int(pay_type)

        # print(request.data)
        # print(amount)
        # 사용자 정보를 불러오는 이유 : 현재 적립금 포인트 정보 확인
        # 결제 후 차감하여 갱신
        member_ins = None
        try:
            member_ins = Member.objects.get(agency_id=agency_id, pk=member_id)
        except Member.DoesNotExist as e:
            pass

        # 첫결제 여부
        isFirst = True
        if member_ins is not None:
            try:
                pay_qs = Payment.objects.filter(
                    agency_id=agency_id, member_id=member_id).all()
                if pay_qs.count() > 0:
                    isFirst = False
            except Payment.DoesNotExist:
                pass

            if pay_type == 0 or pay_type == 2:
                agency_pt_ins = AgencyPoint.objects.get(agency_id=agency_id)
                _point = signUpPoint(agency_id, pay_type)
                print(_point)
                # if datetime.datetime.today().weekday() < 5:
                #     _point = agency_pt_ins.def_day_new
                # else:
                #     _point = agency_pt_ins.def_weekend_new

                if _point:
                    member_ins.point += int(amount) * _point[0] // 100

                    payment = Payment()
                    payment.agency_id = agency_id
                    payment.member_id = member_id
                    payment.save_point = int(amount) * _point[0] // 100
                    payment.pay_type = 1
                    payment.balance_point = member_ins.point
                    if _point[1]:
                        payment.memo = '충전 포인트 적립(이벤트)'
                    else:
                        payment.memo = '충전 포인트 적립'
                    payment.rate = _point[0]
                    payment.tran_dttm = datetime.datetime.now()
                    payment.save()

        # 결제 이력남기기위해
        try:
            payment = Payment()
            payment.agency_id = agency_id
            if member_ins is not None:
                payment.member_id = member_id
            # 결제 타입 선택
            payment.pay_type = pay_type
            if pay_type == 3:
                payment.isKeepMoney = True
            if int(use_point) > 0:
                payment.isPoint = True

            if pay_type == 0 or pay_type == 2:
                if member_ins is not None:
                    payment.save_money = int(amount)  # 결제 금액
                    payment.balance_money = member_ins.money + \
                        int(amount)  # 사용자 현재 잔액 정보
                    member_ins.money = member_ins.money + \
                        int(amount)  # 사용자 현재 잔액 정보
                else:
                    payment.used_money = int(amount)  # 결제 금액
            else:
                payment.used_money = int(amount)  # 결제 금액
                if member_ins is not None:
                    payment.balance_money = member_ins.money - \
                        int(amount)  # 사용자 현재 잔액 정보
                    member_ins.money = member_ins.money - \
                        int(amount)  # 사용자 현재 잔액 정보

            # 적립금 계산
            rate_value = 0
            if member_ins is not None:
                rate = getAgencyRate(agency_id, device_type, pay_type)
                if rate and rate[0] is not None:
                    payment.rate = rate[0]
                    print(rate[0])
                    # print(amount, rate[0])
                    s_amount = int(amount)
                    rate_value = float(s_amount) * float(rate[0]) / 100
                    print(rate_value)
                    payment.save_point = int(rate_value)
                    member_ins.point = member_ins.point + \
                        int(rate_value)  # 잔돈은 사용자 현금잔액으로
                    payment.balance_point = member_ins.point  # 사용자 현재 잔액 정보
                    if rate[1]:
                        payment.memo = '이벤트 포인트 적립'

                # 포인트 계산
                payment.used_point = use_point
                if int(use_point) > 0:
                    member_ins.point = member_ins.point - int(use_point)  # 차감
                    payment.balance_point = member_ins.point
            # 장비
            payment.type = device_type
            # 첫결제 여부
            payment.first = isFirst
            if member_ins is None:
                payment.memo = '비회원 결제'

            payment.tran_dttm = datetime.datetime.now()
            payment.save()
            resp['amount'] = amount
            # 저장
            if member_ins is not None:
                member_ins.last_use_dttm = datetime.datetime.now()
                member_ins.use_count += 1
                member_ins.save()
            resp['success'] = True
        except Payment.DoesNotExist as e:
            print(e)
            resp['success'] = False

        if resp['success']:
            return Response(resp)
        else:
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class AlertInfoViews(
        mixins.ListModelMixin,
        generics.GenericAPIView):

    serializer_class = AlertInfoSerializer
    # (0, '퇴출요청'),   >> args 에 URL 삽입
    # (1, '장난금지'),   >> args 에 URL 삽입
    # (2, '동물퇴출'),   >> args 에 URL 삽입
    # (3, '사이렌'),   >> args 에 URL 삽입
    # (4, '냉난방기 켜기'),  >> 디바이스리스트에서 ctrl 리스트 검색해서 키오스크에 전달
    # (5, '장비전원 재시작'),
    # (6, 'PC재부팅')
    # (7, '코인신호보내기') >> args 에  { ctrl_id, coin } 삽입

    def get_queryset(self, *args, **kwargs):
        #queryset = AlertInfo.objects.filter(agency=self.agency).order_by('reg_dttm')
        # test
        queryset = AlertInfo.objects.filter(
            agency=self.agency, flag=False).order_by('reg_dttm')
        return queryset

    # 테스트 용도로 제거함
    @agency_required
    def get(self, request, *args, **kwargs):
        # return self.list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        # 상태 flag false 처리
        for q in serializer.data:
            al_ins = AlertInfo.objects.get(pk=q['id'])
            al_ins.flag = True
            al_ins.save()
        return Response(serializer.data)


def getAgencyRate(agency_id, device_type, pay_type):
    # (0, '세탁기'),
    # (1, '건조기'),
    # (2, '트롬스타일러'),
    # (3, '운동화세탁기'),
    # (4, '운동화건조기'),
    # (5, '냉난방'),
    # (6, '세탁용품')
    # ['월', '화', '수', '목', '금', '토', '일']
    today = datetime.datetime.today()
    week = today.weekday()

    agency_pt_ins = AgencyPoint.objects.get(agency_id=agency_id)
    ret_rate = 0
    isEvent = False

    if not device_type:
        return

    if int(device_type) == 0:
        if agency_pt_ins.evt_st_date is not None and agency_pt_ins.evt_et_date is not None and \
                today.date() >= agency_pt_ins.evt_st_date and today.date() <= agency_pt_ins.evt_et_date:
            if week < 5:
                ret_rate = agency_pt_ins.evt_day_wash
            else:
                ret_rate = agency_pt_ins.evt_weekend_wash
            isEvent = True
        else:
            if pay_type == 0:
                if week < 5:
                    ret_rate = agency_pt_ins.def_day_wash
                else:
                    ret_rate = agency_pt_ins.def_weekend_wash
            elif pay_type == 2:
                if week < 5:
                    ret_rate = agency_pt_ins.def_card_day_wash
                else:
                    ret_rate = agency_pt_ins.def_card_weekend_wash
    elif int(device_type) == 1:
        if agency_pt_ins.evt_st_date is not None and agency_pt_ins.evt_et_date is not None and \
                today.date() >= agency_pt_ins.evt_st_date and today.date() <= agency_pt_ins.evt_et_date:
            if week < 5:
                ret_rate = agency_pt_ins.evt_day_dry
            else:
                ret_rate = agency_pt_ins.evt_weekend_dry
            isEvent = True
        else:
            if pay_type == 0:
                if week < 5:
                    ret_rate = agency_pt_ins.def_day_dry
                else:
                    ret_rate = agency_pt_ins.def_weekend_dry
            elif pay_type == 2:
                if week < 5:
                    ret_rate = agency_pt_ins.def_card_day_dry
                else:
                    ret_rate = agency_pt_ins.def_card_weekend_dry
    elif int(device_type) == 3:
        if agency_pt_ins.evt_st_date is not None and agency_pt_ins.evt_et_date is not None and \
                today.date() >= agency_pt_ins.evt_st_date and today.date() <= agency_pt_ins.evt_et_date:
            if week < 5:
                ret_rate = agency_pt_ins.evt_day_shoes_wash
            else:
                ret_rate = agency_pt_ins.evt_weekend_shoes_wash
            isEvent = True
        else:
            if pay_type == 0:
                if week < 5:
                    ret_rate = agency_pt_ins.def_day_shoes_wash
                else:
                    ret_rate = agency_pt_ins.def_weekend_shoes_wash
            elif pay_type == 2:
                if week < 5:
                    ret_rate = agency_pt_ins.def_card_day_shoes_wash
                else:
                    ret_rate = agency_pt_ins.def_card_weekend_shoes_wash
    elif int(device_type) == 4:
        if agency_pt_ins.evt_st_date is not None and agency_pt_ins.evt_et_date is not None and \
                today.date() >= agency_pt_ins.evt_st_date and today.date() <= agency_pt_ins.evt_et_date:
            if week < 5:
                ret_rate = agency_pt_ins.evt_day_shoes_dry
            else:
                ret_rate = agency_pt_ins.evt_weekend_shoes_dry
            isEvent = True
        else:
            if pay_type == 0:
                if week < 5:
                    ret_rate = agency_pt_ins.def_day_shoes_dry
                else:
                    ret_rate = agency_pt_ins.def_weekend_shoes_dry
            elif pay_type == 2:
                if week < 5:
                    ret_rate = agency_pt_ins.def_card_day_shoes_dry
                else:
                    ret_rate = agency_pt_ins.def_card_weekend_shoes_dry

    return ret_rate if ret_rate >= 0 else None, isEvent


# 광고 링크 가져가기
class TubeLinkViews(APIView):
    @agency_required
    def get(self, request, *args, **kwargs):
        resp = dict()
        try:
            v = VideoLinkInfo.objects.latest('upd_dttm')
            resp = VideoLinkInfoSerializer(v).data
        except VideoLinkInfo.DoesNotExist:
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        return Response(resp)


class AgencyPointInfo(
        mixins.UpdateModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyPointSerializer

    def get_queryset(self):
        return AgencyPoint.objects.all()

    @agency_required
    def get(self, request, *args, **kwargs):
        instance = AgencyPoint.objects.get(agency=self.agency)
        serializer = AgencyPointSerializer(instance)
        obj = serializer.data
        return Response(obj)

    @agency_required
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


def removeObject(obj):
    obj['member'].pop('pwd')
    obj['member'].pop('black')
    obj['agency'].pop('menu_wash')
    obj['agency'].pop('menu_dry')
    obj['agency'].pop('menu_shoes_wash')
    obj['agency'].pop('menu_shoes_dry')
    obj['agency'].pop('menu_point')
    obj['agency'].pop('menu_air')
    obj['agency'].pop('menu_tromm')
    obj['agency'].pop('menu_item')
    obj['agency'].pop('menu_card')
    obj['agency'].pop('expire_date')
    obj['agency'].pop('cor_number')


class AgencyMemberPayment(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

    pagination_class = None
    serializer_class = PaymentAgencySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Payment.objects.filter(
            agency=self.agency, member_id=self.kwargs['user']).all().order_by('-pay_dttm')

        return queryset

    @agency_required
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
