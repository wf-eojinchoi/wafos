from django.db import models

from device_brand.models import Brand
from device_model.models import Model

class DeviceInfo(models.Model):
    brand = models.ForeignKey(
        'device_brand.Brand',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='member_id')
    model = models.ForeignKey(
        'device_model.Model',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='member_id')
    type = models.IntegerField(
        verbose_name='타입',
        choices=(
            (0, '세탁기'),
            (1, '건조기'),
            # (3, '세탁용품'),
            # (4, '냉난방기')
        ))
    photo = models.TextField(
        null=True,
        default=None,
        verbose_name='장비 이미지')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')
    memo = models.TextField(
        null=True,
        default=None,
        verbose_name='기타 사항')
    # (계약용)
    amount = models.IntegerField(
        null=True,
        default=0,
        verbose_name='가격정보-단가'
    )
    count = models.IntegerField(
        null=True,
        default=0,
        verbose_name='가격정보-수량'
    )
    rate = models.IntegerField(
        null=True,
        default=0,
        verbose_name='가격정보-할인율'
    )
    kg = models.IntegerField(
        null=True,
        default=0,
        verbose_name='가격정보-용량'
    )

    class Meta:
        db_table = 'device_info'
        verbose_name = 'device_info'
