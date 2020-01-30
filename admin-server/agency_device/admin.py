from django.contrib import admin
from .models import AgencyDeviceInfo

# Register your models here.


class AgencyDeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(AgencyDeviceInfo, AgencyDeviceAdmin)
