from django.db import models


class PointHistory(models.Model):
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='member_id')
    point = models.IntegerField(
        default='0',
        verbose_name='발급된 포인트')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    class Meta:
        db_table = 'point'
        verbose_name = '포인트 발행 이력'
