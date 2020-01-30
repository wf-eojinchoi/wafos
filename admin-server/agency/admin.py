from django.contrib import admin
from .models import Agency

# Register your models here.


class AgencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Agency, AgencyAdmin)
