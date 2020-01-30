from django.db import models

# Create your models here.


class Member(models.Model):
    tel = models.CharField(
        max_length=11,
        verbose_name='사용자 전화번호')
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    pwd = models.CharField(
        max_length=256,
        verbose_name='비밀번호')
    money = models.IntegerField(
        default='0',
        verbose_name='현금잔액')
    point = models.IntegerField(
        default='0',
        verbose_name='포인트잔액')
    special_point = models.IntegerField(
        default='0',
        verbose_name='포인트잔액')
    black = models.BooleanField(
        default=False,
        verbose_name='차단된 사용자')
    use_sms = models.BooleanField(
        blank=True,
        default=True,
        verbose_name='SMS 사용여부')
    # old_reg_dttm = models.CharField(
    #     null=True,
    #     max_length=30,
    #     verbose_name='기존 가입일')
    # old_login_dttm = models.CharField(
    #     null=True,
    #     max_length=30,
    #     verbose_name='기존 마지막 로그인')
    last_use_dttm = models.DateTimeField(
        null=True,
        verbose_name='마지막 사용일')
    open_date = models.DateTimeField(
        null=True,
        verbose_name='WAFOS-가입일')
    memo = models.TextField(
        null=True,
        verbose_name='메모')
    use_count = models.IntegerField(
        null=True,
        default='0',
        verbose_name='이용횟수')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='가입일')

    class Meta:
        db_table = 'member'
        verbose_name = '사용자 정보'

class LoginInfo(models.Model):
    tel = models.CharField(
        max_length=11,
        verbose_name='사용자 전화번호')
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    money = models.IntegerField(
        default='0',
        verbose_name='현금잔액')
    point = models.IntegerField(
        default='0',
        verbose_name='포인트잔액')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='로그인시간')

    class Meta:
        db_table = 'login_info'
        verbose_name = '사용자 로그인'
