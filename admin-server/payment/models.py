from django.db import models


class Payment(models.Model):
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
    product_amount = models.IntegerField(
        default=0, null=True,
        verbose_name='상품금')
    save_money = models.IntegerField(
        default=0, null=True,
        verbose_name='현금적립')
    used_money = models.IntegerField(
        default=0, null=True,
        verbose_name='현금사용')
    balance_money = models.IntegerField(
        default=0, null=True,
        verbose_name='현금 잔액')
    save_point = models.IntegerField(
        default=0, null=True,
        verbose_name='포인트부여')
    used_point = models.IntegerField(
        default=0, null=True,
        verbose_name='포인트사용')
    balance_point = models.IntegerField(
        default=0, null=True,
        verbose_name='포인트 잔액')
    type = models.IntegerField(
        null=True,
        verbose_name='타입',
        choices=(
            (0, '세탁기'),
            (1, '건조기'),
            (2, '트롬스타일러'),
            (3, '운동화세탁기'),
            (4, '운동화건조기'),
            (5, '냉난방'),
            (6, '세탁용품')
        ))
    pay_type = models.IntegerField(
        null=True,
        verbose_name='결제타입',
        choices=(
            (0, '현금'),
            (1, '포인트'),
            (2, '카드'),
            (3, '현금잔액이용')
        ))
    first = models.BooleanField(
        default=False,
        verbose_name='첫결제여부')
    use_time = models.IntegerField(
        default=0,
        null=True,
        verbose_name='이용시간/분')
    isPoint = models.BooleanField(
        default=False,
        verbose_name='포인트 사용여부'
    )
    isKeepMoney = models.BooleanField(
        default=False,
        verbose_name='적립금 사용여부'
    )
    memo = models.TextField(
        null=True,
        verbose_name='비고'
    )
    rate = models.IntegerField(
        default=None, null=True,
        verbose_name='할인율')
    pay_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='결제일')
    tran_dttm = models.DateTimeField(
        null=True,
        verbose_name='거래날짜')
    tran_type = models.CharField(
        null=True,
        max_length=6,
        verbose_name='기존 거래타입')

    class Meta:
        db_table = 'payment'
        verbose_name = '결제정보'
