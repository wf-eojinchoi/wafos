from django.db import models


class AgencyDeviceInfo(models.Model):
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    device = models.ForeignKey(
        'device_info.DeviceInfo',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='device_id')
    etcDevice = models.ForeignKey(
        'etc_device.EtcDeviceInfo',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='etc_device_id')
    memo = models.TextField(
        verbose_name='메모'
    )
    current_coin = models.IntegerField(
        default=0,
        verbose_name='기준코인(요금)'
    )
    min_coin = models.IntegerField(
        default=0,
        verbose_name='최소코인(요금)'
    )
    max_coin = models.IntegerField(
        default=0,
        verbose_name='최대코인(요금)'
    )
    controller_id = models.IntegerField(
        default=None, null=True,
        verbose_name='컨트롤러ID'
    )
    capacity = models.IntegerField(
        default=None, null=True,
        verbose_name='용량'
    )
    min_etc_coin = models.IntegerField(
        default=0,
        verbose_name='기준시간(분)'
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

    machine_id = models.IntegerField(
        default=None, null=True,
        verbose_name='장비 ID - 마이그레이션용'
    )


    class Meta:
        db_table = 'agency_device_info'
        verbose_name = '대리점-장비 목록'
