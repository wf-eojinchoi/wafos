from django.contrib import admin
from .models import DeviceInfo

# Register your models here.


class DeviceInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(DeviceInfo, DeviceInfoAdmin)
