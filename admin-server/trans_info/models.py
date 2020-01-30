from django.db import models

# Create your models here.
class TransInfo(models.Model):
    category = models.CharField(
        null=True,
        max_length=150,
        verbose_name='category')
    keyword = models.CharField(
        null=True,
        max_length=150,
        verbose_name='keyword')
    kr = models.TextField(
        null=True,
        default=None,
        verbose_name='kr')
    vn = models.TextField(
        null=True,
        default=None,
        verbose_name='vn')
    en = models.TextField(
        null=True,
        default=None,
        verbose_name='en')
    cn = models.TextField(
        null=True,
        default=None,
        verbose_name='en')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록일')

    class Meta:
        db_table = 'trans_info'
        verbose_name = 'trans_info'