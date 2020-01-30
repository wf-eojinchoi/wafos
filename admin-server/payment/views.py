import calendar
import datetime

from django.conf import settings
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from openpyxl import Workbook
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from agency.models import Agency
from payment.models import Payment
from payment.serializers import PaymentSerializer, PaymentAgencySerializer
from washfriends.settings import WF_HOST_DOMAIN


class PaymentList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Payment.objects.all().order_by('-pay_dttm')

        agency_name = self.request.query_params.get('agency_name', None)
        tel = self.request.query_params.get('tel', None)

        if agency_name is not None:
            try:
                agency_ins = Agency.objects.get(agency_name=agency_name)
                queryset = queryset.filter(agency_id=agency_ins.id)
            except Agency.DoesNotExist:
                pass

        if tel is not None:
            queryset = queryset.filter(member__tel__contains=tel)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PaymentDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AgencyMemberPayment(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PaymentAgencySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Payment.objects.filter(agency_id=self.kwargs['agency'], member_id=self.kwargs['user']).all()

        sortby = self.request.query_params.get('sortby', None)
        descending = self.request.query_params.get('descending', None)
        print(sortby)
        order_by = 'tran_dttm'
        if descending:
            order_by = sortby
        else:
            if sortby is not None:
                order_by = '-' + sortby
        #
        # queryset = queryset.order_by(order_by)

        return queryset.order_by(order_by)

    def get(self, request, *args, **kwargs):
        # return self.list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            obj = serializer.data
            for o in obj:
                removeObject(o)
            # obj.pop('pwd')
            return self.get_paginated_response(obj)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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

class PaymentMonthList(APIView):

    def post(self, request, *args, **kwargs):
        t_year = request.data.get('year', 2019)
        agency_id = request.data.get('agency_id')
        agency_name = request.data.get('agency_name')
        if t_year is None:
            t_year = datetime.datetime.now().year
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        target_date = datetime.datetime(int(t_year), 1, 1).date()
        ###
        total_object = {
            'save_money': 0,
            'used_money': 0,
            'balance_money': 0,
            'save_point': 0,
            'used_point': 0,
            'balance_point': 0,
            'first': 0,
            'type0': 0,
            'type1': 0,
            'type2': 0,
            'type3': 0,
            'type4': 0,
            'type5': 0,
            'type6': 0
        }
        resp = dict()

        array = []
        for month in range(1, 13):
            last_day = calendar.monthrange(int(t_year), month)[1] + 1
            obj = {
                'save_money': 0,
                'used_money': 0,
                'balance_money': 0,
                'save_point': 0,
                'used_point': 0,
                'balance_point': 0,
                'first': 0,
                'date':'%s-%02d' % (t_year, month),
                'type0': 0,
                'type1': 0,
                'type2': 0,
                'type3': 0,
                'type4': 0,
                'type5': 0,
                'type6': 0
            }
            save_money = 0
            used_money = 0
            balance_money = 0
            save_point = 0
            used_point = 0
            balance_point = 0
            for day in range(1, last_day):
                current_date = datetime.datetime(target_date.year, month, day).date()
                if agency_id is not None:
                    pay_qs = Payment.objects.filter(agency_id=agency_id).all()
                elif agency_name is not None:
                    if agency_name == '전체':
                        pay_qs = Payment.objects.all()
                    else:
                        pay_qs = Payment.objects.filter(agency__agency_name__contains=agency_name).all()
                else:
                    pay_qs = Payment.objects.all()
                pay_qs = pay_qs.filter(tran_dttm__date=current_date).all()
                # print('1# ', agency_name, pay_qs.count())
                # print('2# ', agency_name, pay_qs.count())
                for pay_ins in pay_qs:
                    if pay_ins.save_money is not None:
                        save_money += pay_ins.save_money
                    else:
                        pass
                    if pay_ins.used_money is not None:
                        used_money += pay_ins.used_money
                    else:
                        pass
                    if pay_ins.balance_money is not None:
                        balance_money += pay_ins.balance_money
                    else:
                        pass
                    if pay_ins.save_point is not None:
                        save_point += pay_ins.save_point
                    else:
                        pass
                    if pay_ins.used_point is not None:
                        used_point += pay_ins.used_point
                    else:
                        pass
                    if pay_ins.balance_point is not None:
                        balance_point += pay_ins.balance_point
                    else:
                        pass
                    if pay_ins.first:
                        obj['first'] += 1
                    if pay_ins.type is not None:
                        if pay_ins.type == 0:
                            obj['type0'] += 1
                        elif pay_ins.type == 1:
                            obj['type1'] += 1
                        elif pay_ins.type == 2:
                            obj['type2'] += 1
                        elif pay_ins.type == 3:
                            obj['type3'] += 1
                        elif pay_ins.type == 4:
                            obj['type4'] += 1
                        elif pay_ins.type == 5:
                            obj['type5'] += 1
                        elif pay_ins.type == 6:
                            obj['type6'] += 1
                # print('# ', save_money, used_money, balance_money)
                obj['save_money'] = save_money
                obj['used_money'] = used_money
                obj['balance_money'] = balance_money
                obj['save_point'] = save_point
                obj['used_point'] = used_point
                obj['balance_point'] = balance_point
            total_object['save_money'] += obj['save_money']
            total_object['used_money'] += obj['used_money']
            total_object['balance_money'] += obj['balance_money']
            total_object['save_point'] += obj['save_point']
            total_object['used_point'] += obj['used_point']
            total_object['first'] += obj['first']
            total_object['type0'] += obj['type0']
            total_object['type1'] += obj['type1']
            total_object['type2'] += obj['type2']
            total_object['type3'] += obj['type3']
            total_object['type4'] += obj['type4']
            total_object['type5'] += obj['type5']
            total_object['type6'] += obj['type6']

            array.append(obj)
        # serializer = self.get_serializer(queryset, many=True)
        resp['total'] = total_object
        resp['results'] = array
        return Response(resp)


class PaymentDayList(APIView):

    def post(self, request, *args, **kwargs):
        t_year = request.data.get('year')
        t_month = request.data.get('month')
        agency_id = request.data.get('agency_id')
        agency_name = request.data.get('agency_name')
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        target_date = datetime.datetime(int(t_year), int(t_month), 1).date()
        ###
        total_object = {
            'save_money': 0,
            'used_money': 0,
            'balance_money': 0,
            'save_point': 0,
            'used_point': 0,
            'balance_point': 0,
            'first': 0,
            'type0': 0,
            'type1': 0,
            'type2': 0,
            'type3': 0,
            'type4': 0,
            'type5': 0,
            'type6': 0
        }
        resp = dict()
        last_day = calendar.monthrange(target_date.year, target_date.month)[1] + 1
        array = []
        for day in range(1, last_day):
            current_date = datetime.datetime(target_date.year, target_date.month, day).date()
            obj = {
                'save_money': 0,
                'used_money': 0,
                'balance_money': 0,
                'save_point': 0,
                'used_point': 0,
                'balance_point': 0,
                'first': 0,
                'date':'%s' % current_date,
                'type0': 0,
                'type1': 0,
                'type2': 0,
                'type3': 0,
                'type4': 0,
                'type5': 0,
                'type6': 0
            }
            pay_qs = Payment.objects.filter(tran_dttm__date=current_date).all()
            if agency_id is not None:
                pay_qs = pay_qs.filter(agency_id=agency_id)
            if agency_name is not None:
                if agency_name == '전체':
                    pass
                else:
                    pay_qs = pay_qs.filter(agency__agency_name=agency_name)
            save_money = 0
            used_money = 0
            balance_money = 0
            save_point = 0
            used_point = 0
            balance_point = 0
            for pay_ins in pay_qs:
                save_money += pay_ins.save_money if pay_ins.save_money is not None else 0
                used_money += pay_ins.used_money if pay_ins.used_money is not None else 0
                balance_money += pay_ins.balance_money if pay_ins.balance_money is not None else 0
                save_point += pay_ins.save_point if pay_ins.save_point is not None else 0
                used_point += pay_ins.used_point if pay_ins.used_point is not None else 0
                balance_point += pay_ins.balance_point if pay_ins.balance_point is not None else 0
                if pay_ins.first:
                    obj['first'] += 1
                if pay_ins.type is not None:
                    if pay_ins.type == 0:
                        obj['type0'] += 1
                    elif pay_ins.type == 1:
                        obj['type1'] += 1
                    elif pay_ins.type == 2:
                        obj['type2'] += 1
                    elif pay_ins.type == 3:
                        obj['type3'] += 1
                    elif pay_ins.type == 4:
                        obj['type4'] += 1
                    elif pay_ins.type == 5:
                        obj['type5'] += 1
                    elif pay_ins.type == 6:
                        obj['type6'] += 1
            obj['save_money'] = save_money
            obj['used_money'] = used_money
            obj['balance_money'] = balance_money
            obj['save_point'] = save_point
            obj['used_point'] = used_point
            obj['balance_point'] = balance_point

            total_object['save_money'] += obj['save_money']
            total_object['used_money'] += obj['used_money']
            total_object['balance_money'] += obj['balance_money']
            total_object['save_point'] += obj['save_point']
            total_object['used_point'] += obj['used_point']
            total_object['first'] += obj['first']
            total_object['type0'] += obj['type0']
            total_object['type1'] += obj['type1']
            total_object['type2'] += obj['type2']
            total_object['type3'] += obj['type3']
            total_object['type4'] += obj['type4']
            total_object['type5'] += obj['type5']
            total_object['type6'] += obj['type6']

            array.append(obj)
        # serializer = self.get_serializer(queryset, many=True)
        resp['total'] = total_object
        resp['results'] = array
        return Response(resp)

class YearList(APIView):
    def get(self, request, *args, **kwargs):
        resp = dict()
        arr = []
        for y in range(2015, 3100):
            arr.append(y)
        resp['results'] = arr
        resp['now'] = datetime.datetime.now().year
        return Response(resp)



class DnExcel(APIView):
    def post(self, request, *arg, **kwargs):
        resp = dict()
        agency_id = request.data.get('agency_id')
        st_date = request.data.get('st_date')
        et_date = request.data.get('et_date')
        type = request.data.get('type')

        if agency_id is None:
            agency = Agency.objects.get(agency_name=request.data.get('agency_name'))
            agency_id = agency.id

        wb = Workbook()
        ws = wb.active
        if agency_id is not None:
            ws.append(('회원 번호', '거래 일자', '거래 시간', '서비스 종류', '현금 충전', '현금 사용', '포인트 적립', '포인트 사용', '현금 잔액', '포인트 잔액'))
        else:
            ws.append(('가맹점명', '회원 번호', '거래 일자', '거래 시간', '서비스 종류', '현금 충전', '현금 사용', '포인트 적립', '포인트 사용', '현금 잔액', '포인트 잔액'))

        if int(type) is 1:
            start_date = datetime.datetime.strptime(st_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(et_date, "%Y-%m-%d").date()
            if agency_id is not None:
                queryset = Payment.objects.filter(Q(tran_dttm__date__gte=start_date)&Q(tran_dttm__date__lte=end_date),
                                           agency_id=agency_id).all()
            else:
                queryset = Payment.objects.filter(Q(tran_dttm__date__gte=start_date) & Q(tran_dttm__date__lte=end_date)).all()
        else:
            if agency_id is not None:
                queryset = Payment.objects.filter(agency_id=agency_id).all()
            else:
                queryset = Payment.objects.all()

        print(queryset.count())

        for query in queryset:
            print(query.pay_dttm)
            row_data = []
            if agency_id is None:
                row_data.append(query.agency.agency_name)
            row_data.append(query.member.tel)
            row_data.append(datetime.datetime.strftime(query.pay_dttm, '%Y-%m-%d'))
            row_data.append(datetime.datetime.strftime(query.pay_dttm, '%H:%M:%S'))
            TYPE_MAP = [ '세탁기', '건조기', '에어드레셔', '운동화세탁기', '운동화건조기', '냉난방', '세탁용품' ]
            if query.type is not None:
                row_data.append(TYPE_MAP[query.type])
            else:
                row_data.append('-')
            row_data.append(query.save_money)
            row_data.append(query.used_money)
            row_data.append(query.save_point)
            row_data.append(query.used_point)
            row_data.append(query.balance_money)
            row_data.append(query.balance_point)
            # payment_ins = Payment.objects.filter(agency_id=query.agency_id, member_id=query.id, type__isnull=False).all()
            # row_data.append(payment_ins.count())
            # row_data.append(query.memo)
            # resp['%s'%query.tel] = row_data
            ws.append(row_data)

        path_date = datetime.datetime.now().strftime("%Y%m%d")
        import os
        system_path = os.path.join(settings.MEDIA_ROOT, 'tmp', path_date)
        try:
            if not os.path.exists(system_path):
                os.makedirs(system_path)
        except OSError:
            print('OSError')
        if agency_id is not None:
            agency = Agency.objects.get(pk=agency_id)
            path = os.path.join(system_path, '%s_매출현황_%s.xlsx' % (agency.agency_name, path_date))
        else:
            path = os.path.join(system_path, '매출현황_%s.xlsx' % (path_date))
        wb.save(path)

        filename = os.path.basename(path)
        from django.http import FileResponse
        response = FileResponse(open(path, 'rb'),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = "attachment; filename=%s" % filename

        resp['success'] = True
        if agency_id is not None:
            agency = Agency.objects.get(pk=agency_id)
            resp['path'] = WF_HOST_DOMAIN + '/media/tmp/%s/%s_매출현황_%s.xlsx' % (path_date, agency.agency_name, path_date)
        else:
            resp['path'] = WF_HOST_DOMAIN + '/media/tmp/%s/매출현황_%s.xlsx' % (path_date, path_date)
        # return response
        return Response(resp)