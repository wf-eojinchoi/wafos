from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.


class AgencyAccount(models.Model):
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    login_id = models.CharField(
        max_length=256,
        verbose_name='대리점 ID')
    pwd = models.CharField(
        max_length=256,
        verbose_name='비밀번호')
    api_seckey = models.CharField(
        max_length=64,
        verbose_name='API SECRET키')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    is_active = True

    class Meta:
        db_table = 'agency_account'
        verbose_name = '대리점 계정'


class AgencyAccountAuth(object):
    def authenticate(self, request, username=None, password=None):
        if username and password:
            try:
                user = AgencyAccount.objects.get(login_id=username)
                if check_password(password, user.pwd) \
                        and self.user_can_authenticate(user):
                    return user

            except AgencyAccount.DoesNotExist:
                return None
        else:
            if request.user.is_authenticated:
                return AgencyAccount.objects.get(pk=request.user.id)

        return None

    def user_can_authenticate(self, user):
        is_active = getattr(user, 'is_active', False)
        return is_active

    def get_user(self, user_id):
        try:
            user = AgencyAccount.objects.get(pk=user_id)
        except AgencyAccount.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
