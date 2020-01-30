from django.db import models


class EtcDeviceInfo(models.Model):
    name = models.CharField(
        max_length=150,
        null=True,
        verbose_name='장비명')
    photo = models.TextField(
        null=True,
        blank=True,
        verbose_name='장비 이미지')
    type = models.IntegerField(
        verbose_name='타입',
        choices=(
            (2, '트롬스타일러'),
            (3, '운동화세탁기'),
            (4, '운동화건조기'),
            (5, '냉난방'),
            (6, '세탁용품')
        ))
    memo = models.TextField(
        null=True,
        blank=True,
        verbose_name='기타 사항')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')
    #(계약용)
    amount = models.IntegerField(
        default=0,
        verbose_name='가격정보-단가'
    )
    count = models.IntegerField(
        default=0,
        verbose_name='가격정보-수량'
    )
    rate = models.IntegerField(
        default=0,
        verbose_name='가격정보-할인율'
    )

    class Meta:
        db_table = 'etc_device'
        verbose_name = '기타장비'
