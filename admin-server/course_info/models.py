from django.db import models
from agency.models import Agency
from agency_device.models import AgencyDeviceInfo


class CourseInfo(models.Model):
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    agency_device = models.ForeignKey(
        AgencyDeviceInfo,
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_device_id')

    title = models.CharField(
        null=True,
        max_length=150,
        verbose_name='코스 이름')
    title_en = models.CharField(
        null=True,
        max_length=150,
        verbose_name='코스 이름-영어')
    title_vn = models.CharField(
        null=True,
        max_length=150,
        verbose_name='코스 이름-베트남어')

    description = models.TextField(
        null=True,
        verbose_name='코스 설명')
    description_vn = models.TextField(
        null=True,
        verbose_name='코스 설명-베트남어')
    description_en = models.TextField(
        null=True,
        verbose_name='코스 설명-영어')

    amount = models.IntegerField(
        default='0',
        verbose_name='금액')

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
        db_table = 'course_info'
        verbose_name = '코스 정보'



class StandardCourseInfo(models.Model):
    type = models.IntegerField(
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
    title = models.CharField(
        null=True,
        max_length=150,
        verbose_name='코스 이름')
    title_en = models.CharField(
        null=True,
        max_length=150,
        verbose_name='코스 이름-영어')
    title_vn = models.CharField(
        null=True,
        max_length=150,
        verbose_name='코스 이름-베트남어')

    description = models.TextField(
        null=True,
        verbose_name='코스 설명')
    description_vn = models.TextField(
        null=True,
        verbose_name='코스 설명-베트남어')
    description_en = models.TextField(
        null=True,
        verbose_name='코스 설명-영어')

    amount = models.IntegerField(
        default='0',
        verbose_name='금액')

    upd_dttm = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일')

    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    class Meta:
        db_table = 'standard_course_info'
        verbose_name = '표준 코스 정보'
