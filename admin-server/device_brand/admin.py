from django.contrib import admin
from .models import Brand

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand, BrandAdmin)
