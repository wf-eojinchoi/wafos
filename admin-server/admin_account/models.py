from django.contrib.auth.hashers import check_password
from django.db import models

# Create your models here.
class AdminAccount(models.Model):
    login_id = models.CharField(
        max_length=256,
        verbose_name='관리자 ID')
    name = models.CharField(
        default=None, null=True,
        max_length=256,
        verbose_name='관리자 Name')
    pwd = models.CharField(
        max_length=256,
        verbose_name='비밀번호')

    enterMember = models.BooleanField(
        default=False,
        verbose_name='고객관리')
    enterAgency = models.BooleanField(
        default=False,
        verbose_name='가맹점관리')
    enterDevice = models.BooleanField(
        default=False,
        verbose_name='장비관리')
    enterPayment = models.BooleanField(
        default=False,
        verbose_name='매출관리')
    enterHoliday = models.BooleanField(
        default=False,
        verbose_name='휴일관리')
    enterAccount = models.BooleanField(
        default=False,
        verbose_name='관리자계정관리')

    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    is_active = True

    class Meta:
        db_table = 'admin_account'
        verbose_name = '관리자 계정'


class AdminAccountAuth(object):
    def authenticate(self, request, username=None, password=None):
        if username and password:
            try:
                user = AdminAccount.objects.get(login_id=username)
                print('1user_id:', username)
                if check_password(password, user.pwd) \
                        and self.user_can_authenticate(user):
                    return user

            except AdminAccount.DoesNotExist:
                return None
        else:
            if request.user.is_authenticated:
                print('2user_id:', request.user.id)
                return AdminAccount.objects.get(pk=request.user.id)

        return None

    def user_can_authenticate(self, user):
        is_active = getattr(user, 'is_active', True)
        return is_active

    def get_user(self, user_id):
        try:
            print('3user_id:', user_id)
            user = AdminAccount.objects.get(pk=user_id)
        except AdminAccount.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None


class VideoLinkInfo(models.Model):
    link_path = models.TextField(
        null=True,
        verbose_name='유튜브링크'
    )
    used = models.BooleanField(
        default=True,
        verbose_name='사용여부'
    )
    upd_dttm = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    class Meta:
        db_table = 'video_link_info'
        verbose_name = 'wafos 광고 링크'