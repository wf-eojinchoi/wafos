from django.db import models


class Brand(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='제조사명')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    class Meta:
        db_table = 'device_brand'
        verbose_name = '제조사'