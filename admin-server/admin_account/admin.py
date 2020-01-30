from django.contrib import admin
from .models import AdminAccount

# Register your models here.

class AdminAccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdminAccount, AdminAccountAdmin)
