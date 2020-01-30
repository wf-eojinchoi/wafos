import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from agency_account.models import AgencyAccount
from agency_account.serializers import AgencyAccountSerializer


class AgencyAccountList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyAccountSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = AgencyAccount.objects.all()

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AgencyAccountDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyAccountSerializer

    def get_queryset(self):
        return AgencyAccount.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AgencyAccountInitPwd(
        mixins.UpdateModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyAccountSerializer

    def get_queryset(self):
        print(self.request.data.get('id'))
        return AgencyAccount.objects.filter(agency_id=self.request.data.get('id')).all()

    def put(self, request, *args, **kwargs):
        obj = dict()
        print(request.data.get('id'))
        try:
            acc_ins = AgencyAccount.objects.get(agency_id=self.request.data.get('id'))
            acc_ins.pwd = make_password('0000')
            acc_ins.save()
            obj['success'] = True
        except:
            obj['success'] = False

        return Response(obj, status=status.HTTP_200_OK)


class AgencyAccountChangePwd(
        mixins.UpdateModelMixin,
        generics.GenericAPIView):
    serializer_class = AgencyAccountSerializer

    def get_queryset(self):
        print(self.request.data.get('id'))
        return AgencyAccount.objects.filter(agency_id=self.request.data.get('id')).all()

    def put(self, request, *args, **kwargs):
        obj = dict()
        print(request.data.get('id'))
        try:
            acc_ins = AgencyAccount.objects.get(agency_id=self.request.data.get('id'))
            acc_ins.pwd = make_password(request.data.get('pwd'))
            acc_ins.save()
            obj['success'] = True
        except:
            obj['success'] = False

        return Response(obj, status=status.HTTP_200_OK)


class doLogin(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        print(request.data)
        isSuccess = False
        try:
            acc_ins = AgencyAccount.objects.get(login_id=request.data.get('login_id'))
            # check_password(request.data.get('pwd'), acc_ins.pwd)
            # admin_ins.login_id == 'admin' and admin_ins.pwd == '1111'
            print(acc_ins.pwd, acc_ins.login_id)
            if check_password(request.data.get('pwd'), acc_ins.pwd):
                request.session['agency_id'] = acc_ins.id
                request.session.set_expiry(60*60)

                if datetime.datetime.now().date() > acc_ins.agency.expire_date:
                    isSuccess = False
                    resp['msg'] = '유효기간이 만료되었습니다. 고객센터로 문의해주세요.'
                    return Response(resp)
                isSuccess = True
                resp['id'] = acc_ins.agency_id
                resp['expire'] = acc_ins.agency.expire_date.strftime("%Y-%m-%d")
            else:
                resp['msg'] = '비밀번호를 확인해주세요.'
        except AgencyAccount.DoesNotExist:
            resp['msg'] = '아이디를 확인해주세요.'

        resp['success'] = isSuccess

        return Response(resp)