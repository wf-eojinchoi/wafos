from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_account.models import AdminAccount
from admin_account.serializers import AdminAccountSerializer



class AdminAccountList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = AdminAccountSerializer

    # permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        queryset = AdminAccount.objects.all().order_by('reg_dttm')

        return queryset

    def get(self, request, *args, **kwargs):
        print(request.session.get('admin_id'))
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AdminAccountDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    serializer_class = AdminAccountSerializer

    def get_queryset(self):
        return AdminAccount.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data

        return Response(obj)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class doLogin(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        print(request.data)
        isSuccess = False
        try:
            admin_ins = AdminAccount.objects.get(login_id=request.data.get('login_id'))
            # print(admin_ins, 
            #       admin_ins.pwd,
            #       check_password(request.data.get('pwd'), admin_ins.pwd))
            # admin_ins.id == 'admin' and admin_ins.pwd == '1111'
            # check_password(request.data.get('pwd'), admin_ins.pwd)
            # print(admin_ins.id, admin_ins.pwd, admin_ins.login_id)
            if admin_ins.login_id == 'admin' and admin_ins.pwd == '1111':
                request.session['admin_id'] = admin_ins.id
                request.session.set_expiry(60*60)
                isSuccess = True
                resp['admin_id'] = admin_ins.id
                resp['enterMember'] = admin_ins.enterMember
                resp['enterAgency'] = admin_ins.enterAgency
                resp['enterDevice'] = admin_ins.enterDevice
                resp['enterPayment'] = admin_ins.enterPayment
                resp['enterHoliday'] = admin_ins.enterHoliday
                resp['enterAccount'] = admin_ins.enterAccount
            else:
                resp['msg'] = '비밀번호를 확인해주세요.'
        except AdminAccount.DoesNotExist:
            resp['msg'] = '아이디를 확인해주세요.'

        resp['success'] = isSuccess

        return Response(resp)


class InitPWD(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        isSuccess = False
        try:
            admin_ins = AdminAccount.objects.get(pk=kwargs['pk'])
            admin_ins.pwd = make_password('0000')
            admin_ins.save()
            isSuccess = True
        except AdminAccount.DoesNotExist:
            resp['msg'] = '아이디를 확인해주세요.'

        resp['success'] = isSuccess

        return Response(resp)


class ChangePWD(APIView):
    def post(self, request, *args, **kwargs):
        resp = dict()
        print(request.data)
        isSuccess = False
        try:
            admin_ins = AdminAccount.objects.get(pk=request.data.get('id'))

            if check_password(request.data.get('pwd'), admin_ins.pwd):
                print('OK')
                admin_ins.pwd = make_password(request.data.get('pwd2'))
                admin_ins.save()
                isSuccess = True
        except AdminAccount.DoesNotExist:
            resp['msg'] = '아이디를 확인해주세요.'

        resp['success'] = isSuccess

        return Response(resp)
