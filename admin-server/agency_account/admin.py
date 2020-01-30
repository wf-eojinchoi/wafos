from django.contrib import admin
from .models import AgencyAccount

# Register your models here.


class AgencyAccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(AgencyAccount, AgencyAccountAdmin)
