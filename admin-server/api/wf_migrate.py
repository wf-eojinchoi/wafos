import datetime

from django.contrib.auth.hashers import make_password
from django.test import TestCase

# Create your tests here.
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy import create_engine, select, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, session

from agency.models import Agency, AgencyPoint
from agency.serializers import AgencySerializer, AgencyPointSerializer
from agency_account.models import AgencyAccount
from agency_account.serializers import AgencyAccountSerializer
from agency_device.models import AgencyDeviceInfo
from agency_device.serializers import AgencyDeviceInfoSerializer
from course_info.models import CourseInfo
from course_info.serializers import CourseInfoSerializer
from member.models import Member
from payment.models import Payment
from payment.serializers import PaymentSerializer
from wafos_database.wafos_model import ShopInfo, ShopMenu, PointRule, CustomerInfo, CashPointTran, Machine, WashCourse
from wafos_database.database import conn, engine, db_session


class WFMigrate(APIView):
    def get(self, request, *args, **kwargs):
        response = dict()
        inspector = inspect(engine)
        shop_id = kwargs['sid']
        q_count = db_session.query(ShopInfo).filter_by(ShopID=shop_id).count()
        agency = db_session.query(ShopInfo).filter_by(ShopID=shop_id).all()
        if q_count > 0:

            for a in agency:
                try:
                    Agency.objects.get(agency_code=a.ShopCode)
                except Agency.DoesNotExist:
                    # 가맹점
                    agency = Agency(agency_code=a.ShopCode, agency_name=a.ShopName, agency_owner=a.OwnerName,
                                    addr1=a.Address, cor_number=a.BusinessNumber, phone=a.Phone)
                    agency.expire_date = datetime.datetime.strptime(a.Maintenance, "%Y-%m-%d").date()
                    agency.memo = a.Memo
                    q_menu = db_session.query(ShopMenu).filter_by(ShopID=shop_id).order_by(ShopMenu.id.desc()).first()
                    agency.menu_wash = True if q_menu.menu_wash == '1' else False
                    agency.menu_dry = True if q_menu.menu_dry == '1' else False
                    agency.menu_shoes_wash = True if q_menu.menu_shoes_wash == '1' else False
                    agency.menu_shoes_dry = True if q_menu.menu_shoes_dry == '1' else False
                    agency.menu_item = True if q_menu.menu_item == '1' else False
                    agency.menu_point = True if q_menu.menu_point == '1' else False
                    agency.menu_air = True if q_menu.menu_air == '1' else False
                    agency.save() #save
                    response['agency'] = AgencySerializer(agency).data
                    response['menu'] = '%s%s%s%s%s%s%s' % (q_menu.menu_wash, q_menu.menu_dry, q_menu.menu_shoes_wash,
                                              q_menu.menu_shoes_dry, q_menu.menu_item, q_menu.menu_point, q_menu.menu_air)

                    # 가맹점 계정 생성
                    import hashlib
                    hashkey = hashlib.sha1()
                    hashkey.update(a.ShopCode.encode('utf-8'))
                    agency_account = AgencyAccount(agency_id=agency.id, login_id=agency.agency_code, pwd=make_password(a.Password), api_seckey=hashkey.hexdigest())
                    agency_account.save() #save
                    response['agency_account'] = AgencyAccountSerializer(agency_account).data

                    # 가맹점 포인트
                    q_point = db_session.query(PointRule).filter_by(ShopID=shop_id).order_by(PointRule.id.desc()).first()
                    agency_point = AgencyPoint(agency_id=agency.id)
                    agency_point.def_day_new = q_point.NormalWeekNew if q_point.NormalWeekNew is not None else 0
                    agency_point.def_day_wash = q_point.NormalWeekWash if q_point.NormalWeekWash is not None else 0
                    agency_point.def_day_dry = q_point.NormalWeekDry if q_point.NormalWeekDry is not None else 0
                    agency_point.def_day_shoes_wash = q_point.NormalWeekShoeWash if q_point.NormalWeekShoeWash is not None else 0
                    agency_point.def_day_shoes_dry = q_point.NormalWeekShoeDry if q_point.NormalWeekShoeDry is not None else 0
                    agency_point.def_weekend_new = q_point.NormalWeekendNew if q_point.NormalWeekendNew is not None else 0
                    agency_point.def_weekend_wash = q_point.NormalWeekendWash if q_point.NormalWeekendWash is not None else 0
                    agency_point.def_weekend_dry = q_point.NormalWeekendDry if q_point.NormalWeekendDry is not None else 0
                    agency_point.def_weekend_shoes_wash = q_point.NormalWeekendShoeWash if q_point.NormalWeekendShoeWash is not None else 0
                    agency_point.def_weekend_shoes_dry = q_point.NormalWeekendShoeDry if q_point.NormalWeekendShoeDry is not None else 0
                    
                    agency_point.def_card_day_new = q_point.CardWeekNew if q_point.CardWeekNew is not None else 0
                    agency_point.def_card_day_wash = q_point.CardWeekWash if q_point.CardWeekWash is not None else 0
                    agency_point.def_card_day_dry = q_point.CardWeekDry if q_point.CardWeekDry is not None else 0
                    agency_point.def_card_day_shoes_wash = q_point.CardWeekShoeWash if q_point.CardWeekShoeWash is not None else 0
                    agency_point.def_card_day_shoes_dry = q_point.CardWeekShoeDry if q_point.CardWeekShoeDry is not None else 0
                    agency_point.def_card_weekend_new = q_point.CardWeekendNew if q_point.CardWeekendNew is not None else 0
                    agency_point.def_card_weekend_wash = q_point.CardWeekendWash if q_point.CardWeekendWash is not None else 0
                    agency_point.def_card_weekend_dry = q_point.CardWeekendDry if q_point.CardWeekendDry is not None else 0
                    agency_point.def_card_weekend_shoes_wash = q_point.CardWeekendShoeWash if q_point.CardWeekendShoeWash is not None else 0
                    agency_point.def_card_weekend_shoes_dry = q_point.CardWeekendShoeDry if q_point.CardWeekendShoeDry is not None else 0

                    agency_point.evt_day_new = q_point.EventWeekNew if q_point.EventWeekNew is not None else 0
                    agency_point.evt_day_wash = q_point.EventWeekWash if q_point.EventWeekWash is not None else 0
                    agency_point.evt_day_dry = q_point.EventWeekDry if q_point.EventWeekDry is not None else 0
                    agency_point.evt_day_shoes_wash = q_point.EventWeekShoeWash if q_point.EventWeekShoeWash is not None else 0
                    agency_point.evt_day_shoes_dry = q_point.EventWeekShoeDry if q_point.EventWeekShoeDry is not None else 0
                    agency_point.evt_weekend_new = q_point.EventWeekendNew if q_point.EventWeekendNew is not None else 0
                    agency_point.evt_weekend_wash = q_point.EventWeekendWash if q_point.EventWeekendWash is not None else 0
                    agency_point.evt_weekend_dry = q_point.EventWeekendDry if q_point.EventWeekendDry is not None else 0
                    agency_point.evt_weekend_shoes_wash = q_point.EventWeekendShoeWash if q_point.EventWeekendShoeWash is not None else 0
                    agency_point.evt_weekend_shoes_dry = q_point.EventWeekendShoeDry if q_point.EventWeekendShoeDry is not None else 0
                    if q_point.EventDateFrom is not None and q_point.EventDateFrom is not '0':
                        try:
                            agency_point.evt_st_date = datetime.datetime.strptime(q_point.EventDateFrom, "%Y%m%d").date()
                        except ValueError:
                            pass
                    if q_point.EventDateTo is not None and q_point.EventDateTo is not '0':
                        try:
                            agency_point.evt_et_date = datetime.datetime.strptime(q_point.EventDateTo, "%Y%m%d").date()
                        except ValueError:
                            pass
                    agency_point.save() #save
                    response['agency_point'] = AgencyPointSerializer(agency_point).data




        # qPoint = db_session.query(ShopMenu).filter_by(ShopID=1).first()
        # print(qPoint.menu_wash)
        return Response(response)

class WFMigrateUser(APIView):
    def get(self, request, *args, **kwargs):
        response = dict()
        inspector = inspect(engine)
        shop_id = kwargs['sid']
        q_count = db_session.query(ShopInfo).filter_by(ShopID=shop_id).count()
        agency = db_session.query(ShopInfo).filter_by(ShopID=shop_id).all()
        if q_count > 0:
            for a in agency:
                try:
                    print(a.ShopCode)
                    agency_ins = Agency.objects.get(agency_code=a.ShopCode)
                    # 가맹점 - 회원
                    q_memo_count = db_session.query(CustomerInfo).filter_by(ShopID=shop_id).order_by(
                        CustomerInfo.ShopID.desc()).count()
                    q_memo = db_session.query(CustomerInfo).filter_by(ShopID=shop_id).order_by(
                        CustomerInfo.ShopID.desc()).all()
                    print(q_memo_count)
                    cnt = 0
                    for m in q_memo:
                        tel = m.tel.replace('-', '')
                        try:
                            Member.objects.get(agency_id=agency_ins.id, tel=tel)
                        except Member.DoesNotExist:
                            member = Member(agency_id=agency_ins.id, tel=tel, pwd=m.pwd,
                                            money=m.money, point=m.point, use_count=m.use_count, memo=m.memo)
                            print(m.reg_dttm, type(m.reg_dttm))
                            # dd = datetime.datetime.strptime(m.reg_dttm, "%Y-%m-%d %H:%M:%S")
                            member.open_date = m.reg_dttm  # datetime.datetime.strptime(m.reg_dttm, "%Y-%m-%d %H:%M:%S")
                            member.last_use_dttm = m.last_use_dttm  # datetime.datetime.strptime(m.last_use_dttm, "%Y-%m-%d %H:%M:%S")
                            member.save()
                        # cnt+=1
                        # if cnt == 3:
                        #     return Response({'msg': '테스트'})
                except Agency.DoesNotExist:
                    response['msg'] = 'agency 등록 안됨'
        return Response(response)

class WFMigratePay(APIView):
    def get(self, request, *args, **kwargs):
        response = dict()
        log = []
        inspector = inspect(engine)
        shop_id = kwargs['sid']
        if shop_id == 1114:
            Payment.objects.all().delete()
            return Response({'msg':'clear'})
        q_count = db_session.query(ShopInfo).filter_by(ShopID=shop_id).count()
        agency = db_session.query(ShopInfo).filter_by(ShopID=shop_id).all()
        if q_count > 0:
            for a in agency:
                try:
                    # print(a.ShopCode)
                    agency_ins = Agency.objects.get(agency_code=a.ShopCode)
                    # 가맹점 - 회원
                    q_memo_count = db_session.query(CashPointTran).filter_by(ShopID=shop_id).order_by(
                        CashPointTran.ShopID.desc()).count()
                    q_memo = db_session.query(CashPointTran).filter_by(ShopID=shop_id).order_by(
                        CashPointTran.ShopID.desc()).all()
                    print(q_memo_count)
                    cnt = 0
                    for m in q_memo:
                        kkkk = dict()
                        tel = m.tel.replace('-', '')
                        print(tel)
                        try:
                            mIns = Member.objects.get(agency_id=agency_ins.id, tel=tel)
                            try:
                                pay_i = Payment.objects.get(agency_id=agency_ins.id, memo=m.tel, member_id=mIns.id, tran_dttm=m.tran_dttm)
                                kkkk['pass'] = 'SHOP:%s, %s' % (m.ShopID, tel)
                                kkkk['tran_dttm'] = pay_i.tran_dttm
                                kkkk['target'] = m.tran_dttm
                                aa = datetime.datetime(pay_i.tran_dttm.year, pay_i.tran_dttm.month, pay_i.tran_dttm.day,
                                                       pay_i.tran_dttm.hour, pay_i.tran_dttm.minute, pay_i.tran_dttm.second)
                                kkkk['target-aa'] = aa
                                if aa is not m.tran_dttm:
                                    pay_ins = Payment(agency_id=agency_ins.id, member_id=mIns.id)
                                    pay_ins.used_money = m.cash_out
                                    pay_ins.save_money = m.cash_in
                                    pay_ins.balance_money = m.cash_bal
                                    pay_ins.used_point = m.point_out
                                    pay_ins.save_point = m.point_in
                                    pay_ins.balance_point = m.point_bal
                                    pay_ins.pay_type = 0
                                    pay_ins.tran_type = m.tran_type
                                    pay_ins.tran_dttm = m.tran_dttm
                                    pay_ins.memo = m.tel
                                    pay_ins.save()
                                # log.append(kkkk)
                                # return Response(log)
                            except Payment.DoesNotExist:
                                pay_ins = Payment(agency_id=agency_ins.id, member_id=mIns.id)
                                pay_ins.used_money = m.cash_out
                                pay_ins.save_money = m.cash_in
                                pay_ins.balance_money = m.cash_bal
                                pay_ins.used_point = m.point_out
                                pay_ins.save_point = m.point_in
                                pay_ins.balance_point = m.point_bal
                                pay_ins.pay_type = 0
                                pay_ins.tran_type = m.tran_type
                                pay_ins.tran_dttm = m.tran_dttm
                                pay_ins.memo = m.tel
                                # kkkk = PaymentSerializer(pay_ins).data
                                # log.append(kkkk)
                                pay_ins.save()
                        except Member.DoesNotExist:
                            try:
                                pay_i = Payment.objects.get(agency_id=agency_ins.id, memo=m.tel, tran_dttm=m.tran_dttm)
                                kkkk['pass'] = 'SHOP:%s, %s' % (m.ShopID, tel)
                                kkkk['tran_dttm'] = pay_i.tran_dttm
                                kkkk['target'] = m.tran_dttm
                                aa = datetime.datetime(pay_i.tran_dttm.year, pay_i.tran_dttm.month, pay_i.tran_dttm.day,
                                                       pay_i.tran_dttm.hour, pay_i.tran_dttm.minute, pay_i.tran_dttm.second)
                                kkkk['target-aa'] = aa
                                if aa is not m.tran_dttm:
                                    pay_ins = Payment(agency_id=agency_ins.id)
                                    pay_ins.used_money = m.cash_out
                                    pay_ins.save_money = m.cash_in
                                    pay_ins.balance_money = m.cash_bal
                                    pay_ins.used_point = m.point_out
                                    pay_ins.save_point = m.point_in
                                    pay_ins.balance_point = m.point_bal
                                    pay_ins.pay_type = 0
                                    pay_ins.tran_type = m.tran_type
                                    pay_ins.tran_dttm = m.tran_dttm
                                    pay_ins.memo = m.tel
                                    pay_ins.save()
                                log.append(kkkk)
                            except Payment.DoesNotExist:
                                pay_ins = Payment(agency_id=agency_ins.id)
                                pay_ins.used_money = m.cash_out
                                pay_ins.save_money = m.cash_in
                                pay_ins.balance_money = m.cash_bal
                                pay_ins.used_point = m.point_out
                                pay_ins.save_point = m.point_in
                                pay_ins.balance_point = m.point_bal
                                pay_ins.pay_type = 0
                                pay_ins.tran_type = m.tran_type
                                pay_ins.tran_dttm = m.tran_dttm
                                pay_ins.memo = m.tel
                                # kkkk = PaymentSerializer(pay_ins).data
                                # log.append(kkkk)
                                pay_ins.save()
                        # cnt+=1
                        # if cnt == 13:
                    # return Response({'msg': log})
                except Agency.DoesNotExist:
                    response['msg'] = 'agency 등록 안됨'
        response['count'] = Payment.objects.all().count()
        # response['log'] = log
        return Response(response)


class WFMigrateDevice(APIView):
    def get(self, request, *args, **kwargs):
        response = dict()
        log = []
        inspector = inspect(engine)
        shop_id = kwargs['sid']
        q_count = db_session.query(ShopInfo).filter_by(ShopID=shop_id).count()
        agency = db_session.query(ShopInfo).filter_by(ShopID=shop_id).all()
        if q_count > 0:
            for a in agency:
                try:
                    # print(a.ShopCode)
                    agency_ins = Agency.objects.get(agency_code=a.ShopCode)
                    # 가맹점 - 회원
                    q_memo_count = db_session.query(Machine).filter_by(ShopID=shop_id).order_by(
                        Machine.controller_id).count()
                    q_memo = db_session.query(Machine).filter_by(ShopID=shop_id).order_by(
                        Machine.controller_id).all()
                    print(q_memo_count)
                    cnt = 0
                    for m in q_memo:
                        kkkk = dict()
                        try:
                            mIns = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, controller_id=m.controller_id)
                        except AgencyDeviceInfo.DoesNotExist:
                            kkkk['c_id'] = m.controller_id
                            ad_ins = AgencyDeviceInfo(controller_id=m.controller_id)
                            ad_ins.agency_id=agency_ins.id
                            if m.status == '130001':
                                ad_ins.used = True
                            else:
                                ad_ins.used = False
                            if m.kg is not None:
                                ad_ins.capacity = int(m.kg)
                            ad_ins.current_coin = m.current_coin
                            ad_ins.min_coin = m.min_coin
                            ad_ins.max_coin = m.max_coin
                            ad_ins.min_etc_coin = m.min_etc_coin if m.min_etc_coin is not None else 0
                            print(type(m.MachineKind))
                            # 관리자 보고 ID 따서 해야함.
                            if m.MachineKind == '100001':  # 세탁기
                                ad_ins.device_id = 1
                            elif m.MachineKind == '100002':  # 건조기
                                ad_ins.device_id = 2
                            elif m.MachineKind == '100003':  # 운동화세탁
                                ad_ins.etcDevice_id = 1
                            elif m.MachineKind == '100004':  # 운동화건조
                                ad_ins.etcDevice_id = 2
                            elif m.MachineKind == '100007':  # 냉난방기
                                ad_ins.etcDevice_id = 4
                            elif m.MachineKind == '100005':  # 바운스
                                ad_ins.etcDevice_id = 3
                            elif m.MachineKind == '100008':  # 스타일
                                ad_ins.etcDevice_id = 5
                            ad_ins.machine_id = m.machine_id
                            # kkkk = AgencyDeviceInfoSerializer(ad_ins).data
                            # log.append(kkkk)
                            ad_ins.save()
                        # cnt+=1
                        # if cnt == 13:
                    # return Response({'msg': log})
                    response['msg'] = '등록'
                except Agency.DoesNotExist:
                    response['msg'] = 'agency 등록 안됨'
        # response['count'] = Payment.objects.all().count()
        # response['log'] = log
        return Response(response)


class WFMigrateCourse(APIView):
    def get(self, request, *args, **kwargs):
        response = dict()
        log = []
        inspector = inspect(engine)
        shop_id = kwargs['sid']
        q_count = db_session.query(ShopInfo).filter_by(ShopID=shop_id).count()
        agency = db_session.query(ShopInfo).filter_by(ShopID=shop_id).all()
        if q_count > 0:
            for a in agency:
                try:
                    # print(a.ShopCode)
                    agency_ins = Agency.objects.get(agency_code=a.ShopCode)
                    # 가맹점 - 회원
                    q_memo_count = db_session.query(WashCourse).filter_by(ShopID=shop_id).order_by(
                        WashCourse.machine_id).count()
                    q_memo = db_session.query(WashCourse).filter_by(ShopID=shop_id).order_by(
                        WashCourse.machine_id).all()
                    print(q_memo_count)
                    cnt = 0
                    for m in q_memo:
                        kkkk = dict()
                        try:
                            mIns = CourseInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                        except CourseInfo.MultipleObjectsReturned:
                            pass
                        except CourseInfo.DoesNotExist:
                            # 관리자 보고 ID 따서 해야함
                            if m.CourseName1 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName1
                                c_ins.description = m.Description1
                                c_ins.amount = m.Fare1
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                            if m.CourseName2 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName2
                                c_ins.description = m.Description2
                                c_ins.amount = m.Fare2
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                            if m.CourseName3 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName3
                                c_ins.description = m.Description3
                                c_ins.amount = m.Fare3
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                            if m.CourseName4 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName4
                                c_ins.description = m.Description4
                                c_ins.amount = m.Fare4
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                            if m.CourseName5 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName5
                                c_ins.description = m.Description5
                                c_ins.amount = m.Fare5
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                            if m.CourseName6 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName6
                                c_ins.description = m.Description6
                                c_ins.amount = m.Fare6
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                            if m.CourseName7 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName7
                                c_ins.description = m.Description7
                                c_ins.amount = m.Fare7
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                            if m.CourseName8 is not None:
                                ad_ins = AgencyDeviceInfo.objects.get(agency_id=agency_ins.id, machine_id=m.machine_id)
                                c_ins = CourseInfo(agency_id=agency_ins.id)
                                c_ins.machine_id = m.machine_id
                                c_ins.agency_device_id = ad_ins.id
                                c_ins.title = m.CourseName8
                                c_ins.description = m.Description8
                                c_ins.amount = m.Fare8
                                c_ins.save()
                                log.append(CourseInfoSerializer(c_ins).data)
                        # cnt+=1
                        # if cnt == 13:
                    # return Response({'msg': log})
                    response['msg'] = '등록'
                except Agency.DoesNotExist:
                    response['msg'] = 'agency 등록 안됨'
        # response['count'] = Payment.objects.all().count()
        response['log'] = log
        return Response(response)