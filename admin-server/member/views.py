import datetime

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db.models import Q, F
from django.shortcuts import render

# Create your views here.
from openpyxl import Workbook
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from agency.models import Agency
from member.models import Member
from member.serializers import MemberSerializer
from payment.models import Payment


class MemberList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Member.objects.all()  # .order_by('last_use_dttm')
        sortby = self.request.query_params.get('sortby', 'last_use_dttm')
        descending = self.request.query_params.get('descending', None)
        agency_name = self.request.query_params.get('agency_name', None)
        tel = self.request.query_params.get('tel', None)
        print(agency_name)
        if agency_name is not None:
            try:
                if agency_name == '전체':
                    pass
                else:
                    agency_ins = Agency.objects.get(agency_name=agency_name)
                    queryset = queryset.filter(agency_id=agency_ins.id)
            except Agency.DoesNotExist:
                pass

        if tel is not None:
            queryset = queryset.filter(tel__contains=tel)

        if sortby == 'adsf':
            sortby = 'agency__agency_name'
        # order_by = ''
        # if sortby == 'rvd_date':
        #     order_by = 'rvd_date'
        # elif sortby == 'stat':
        #     order_by = 'stat'
        # else:
        #     order_by = 'id'
        #
        # if descending:
        #     order_by = '-' + order_by
        #
        # queryset = queryset.order_by(order_by)
        # if descending:
        #     sortby = '-' + sortby

        # return queryset.order_by(F(sortby).desc(nulls_last=True))#order_by(sortby)
        if descending:
            return queryset.order_by(F(sortby).desc(nulls_last=True))#order_by(order_by)
        else:
            return queryset.order_by(F(sortby).asc(nulls_last=True))  # order_by(order_by)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MemberDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data
        print('#')
        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AgencyMemberList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Member.objects.filter(agency_id=self.kwargs['pk']).all()
        sortby = self.request.query_params.get('sortby', None)
        descending = self.request.query_params.get('descending', None)
        agency_name = self.request.query_params.get('agency_name', None)
        tel = self.request.query_params.get('tel', None)
        print('Agency Member:', sortby)
        if agency_name is not None:
            try:
                agency_ins = Agency.objects.get(agency_name=agency_name)
                queryset = queryset.filter(agency_id=agency_ins.id)
            except Agency.DoesNotExist:
                pass

        if tel is not None:
            queryset = queryset.filter(tel__contains=tel)
        # order_by = ''
        # if sortby == 'rvd_date':
        #     order_by = 'rvd_date'
        # elif sortby == 'stat':
        #     order_by = 'stat'
        # else:
        #     order_by = 'id'
        #
        if sortby:
            # if descending:
            order_by = sortby
            # else:
            #     order_by = '-' + sortby
        else:
            order_by = 'id'
        #
        # queryset = queryset.order_by(order_by)
        if descending:
            return queryset.order_by(F(order_by).desc(nulls_last=True))#order_by(order_by)
        else:
            return queryset.order_by(F(order_by).asc(nulls_last=True))  # order_by(order_by)

    def get(self, request, *args, **kwargs):
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

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AgencyMemberDetail(APIView):

    def get(self, request, *args, **kwargs):
        instance = Member.objects.get(pk=kwargs['user'])
        serializer = MemberSerializer(instance)

        obj = serializer.data
        removeObject(obj)
        print('#')
        return Response(obj)


def removeObject(obj):
    obj.pop('pwd')
    obj.pop('black')
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


class MemberChangePoint(APIView):
    def post(self, request, *arg, **kwargs):
        resp = dict()
        id = request.data.get('id')
        point = request.data.get('point')
        isMinus = request.data.get('minus')
        admin = request.data.get('admin', False)

        mem_ins = Member.objects.get(pk=id)
        memo = None
        if mem_ins.point is not None:
            if isMinus:
                point = int(point) * -1
                mem_ins.point = int(mem_ins.point) + point
                if admin:
                    memo = '관리자포인트감액'
                else:
                    memo = '점주포인트감액'
            else:
                mem_ins.point = int(mem_ins.point) + int(point)
                if admin:
                    memo = '관리자포인트증액'
                else:
                    memo = '점주포인트증액'
        else:
            mem_ins.point = point
        mem_ins.save()
        resp['success'] = True
        Payment(member_id=id, agency_id=mem_ins.agency_id,
                balance_point=mem_ins.point,
                tran_dttm=datetime.datetime.now(),
                save_point=point, memo=memo).save()
        return Response(resp)


class MemberChangeMoney(APIView):
    def post(self, request, *arg, **kwargs):
        resp = dict()
        id = request.data.get('id')
        money = request.data.get('money')
        isMinus = request.data.get('minus')
        admin = request.data.get('admin', False)

        mem_ins = Member.objects.get(pk=id)
        memo = None
        if mem_ins.point is not None:
            if isMinus:
                money = int(money) * -1
                mem_ins.money = int(mem_ins.money) + money
                if admin:
                    memo = '관리자현금감액'
                else:
                    memo = '점주현금감액'
            else:
                mem_ins.money = int(mem_ins.money) + int(money)
                if admin:
                    memo = '관리자현금증액'
                else:
                    memo = '점주현금증액'
        else:
            mem_ins.money = money
        mem_ins.save()
        resp['success'] = True
        Payment(member_id=id, agency_id=mem_ins.agency_id,
                balance_money=mem_ins.money,
                tran_dttm=datetime.datetime.now(),
                save_money=money, memo=memo).save()
        return Response(resp)


class MemberInitPwd(APIView):
    def post(self, request, *arg, **kwargs):
        resp = dict()
        id = request.data.get('id')
        pwd = request.data.get('pwd')
        admin = request.data.get('admin', False)

        if pwd is None:
            pwd = '0000'

        mem_ins = Member.objects.get(pk=id)
        mem_ins.pwd = pwd  # make_password('0000')
        mem_ins.save()
        resp['success'] = True
        print('%s]] PASSWROD 초기화 - member_id[' %
              ('관리자' if admin else '가맹점'), id, ']', datetime.datetime.now(), 'pwd:', pwd)
        return Response(resp)


class MemberChangeMemo(APIView):
    def post(self, request, *arg, **kwargs):
        resp = dict()
        id = request.data.get('id')
        memo = request.data.get('memo')
        admin = request.data.get('admin', False)

        mem_ins = Member.objects.get(pk=id)
        before_memo = mem_ins.memo
        mem_ins.memo = memo
        mem_ins.save()
        resp['success'] = True
        print('%s]] MEMO 변경 - member_id[' % ('관리자' if admin else '가맹점'), id,
              ']', datetime.datetime.now(), ' before:', before_memo, 'after:', memo)
        return Response(resp)


class DnExcel(APIView):
    def post(self, request, *arg, **kwargs):
        resp = dict()
        agency_id = request.data.get('agency_id')
        st_date = request.data.get('st_date')
        et_date = request.data.get('et_date')
        type = request.data.get('type')

        wb = Workbook()
        ws = wb.active
        if agency_id is not None:
            ws.append(('전화번호', '현금잔액', '포인트잔액', '최종이용일', '가입일', '이용건수', '메모'))
        else:
            ws.append(('가맹점명', '전화번호', '현금잔액', '포인트잔액',
                       '최종이용일', '가입일', '이용건수', '메모'))

        if int(type) is 1:
            start_date = datetime.datetime.strptime(st_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(et_date, "%Y-%m-%d").date()
            if agency_id is not None:
                queryset = Member.objects.filter(Q(reg_dttm__date__gte=start_date) & Q(reg_dttm__date__lte=end_date),
                                                 agency_id=agency_id).all()
            else:
                queryset = Member.objects.filter(
                    Q(reg_dttm__date__gte=start_date) & Q(reg_dttm__date__lte=end_date)).all()
        else:
            if agency_id is not None:
                queryset = Member.objects.filter(agency_id=agency_id).all()
            else:
                queryset = Member.objects.all()

        for query in queryset:
            print('#', query.tel)
            row_data = []
            if agency_id is None:
                row_data.append(query.agency.agency_name)
            row_data.append(query.tel)
            row_data.append(query.money)
            row_data.append(query.point)
            row_data.append(query.last_use_dttm)
            row_data.append(query.reg_dttm)
            payment_ins = Payment.objects.filter(
                agency_id=query.agency_id, member_id=query.id, type__isnull=False).all()
            row_data.append(payment_ins.count())
            row_data.append(query.memo)
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
            path = os.path.join(system_path, '%s_고객명부_%s.xlsx' %
                                (agency.agency_name, path_date))
        else:
            path = os.path.join(system_path, 'member_%s.xlsx' % path_date)
        wb.save(path)

        filename = os.path.basename(path)
        from django.http import FileResponse
        response = FileResponse(open(path, 'rb'),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = "attachment; filename=%s" % filename

        resp['success'] = True
        from washfriends.settings import WF_HOST_DOMAIN
        if agency_id is not None:
            agency = Agency.objects.get(pk=agency_id)
            resp['path'] = WF_HOST_DOMAIN + \
                '/media/tmp/%s/%s_고객명부_%s.xlsx' % (path_date,
                                                   agency.agency_name, path_date)
        else:
            resp['path'] = WF_HOST_DOMAIN + \
                '/media/tmp/%s/member_%s.xlsx' % (path_date, path_date)
        # return response
        return Response(resp)
