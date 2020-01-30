from django.db import models


class UserHistory(models.Model):
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    member = models.ForeignKey(
        'member.Member',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='member_id')
    # amount = models.IntegerField(
    #     verbose_name='이용금액')
    type = models.IntegerField(
        verbose_name='이용 타입',
        choices=(
            (0, '세탁기'),
            (1, '건조기')
        ))
    type_keyword = models.TextField(
        null=True,
        default=None,
        verbose_name='장비 명')
    use_money = models.IntegerField(
        default=0,
        verbose_name='현금사용')
    use_point = models.IntegerField(
        default=0,
        verbose_name='포인트사용')
    save_money = models.IntegerField(
        default=0,
        verbose_name='현금적립')
    save_point = models.IntegerField(
        default=0,
        verbose_name='포인트 부여')
    balance_money = models.IntegerField(
        default=0,
        verbose_name='현금 잔액')
    balance_point = models.IntegerField(
        default=0,
        verbose_name='포인트 잔액')
    use_time = models.IntegerField(
        default=0,
        verbose_name='이용시간/분')
    use_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='사용일')

    class Meta:
        db_table = 'user_history'
        verbose_name = '사용이력'
