from django.db import models


class Model(models.Model):
    brand = models.ForeignKey(
        'device_brand.Brand',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='brand_id')
    name = models.CharField(
        max_length=120,
        verbose_name='모델명')
    serial = models.CharField(
        max_length=120, null=True,
        default=None,
        verbose_name='시리얼')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    class Meta:
        db_table = 'device_model'
        verbose_name = '모델'
