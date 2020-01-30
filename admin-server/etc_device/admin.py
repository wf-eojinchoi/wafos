from django.contrib import admin
from .models import EtcDeviceInfo

# Register your models here.


class EtcDeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(EtcDeviceInfo, EtcDeviceAdmin)
