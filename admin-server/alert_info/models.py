from django.db import models

# Create your models here.


class AlertInfo(models.Model):
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    cmd = models.IntegerField(
        verbose_name='command',
        choices=(
            (0, '퇴출요청'),
            (1, '장난금지'),
            (2, '동물퇴출'),
            (3, '사이렌'),
            (4, '냉난방기 켜기'),
            (5, '장비전원 재시작'),
            (6, 'PC재부팅')
        ))
    args = models.TextField(
        null=True, blank=True,
        verbose_name='Argument')
    flag = models.BooleanField(
        default=False,
        verbose_name='사용유무 확인'
    )
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    is_active = True

    class Meta:
        db_table = 'alert_info'
        verbose_name = '경고방송 or 기기 제어 관련 CMD'
