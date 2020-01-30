from django.contrib import admin
from .models import Model

# Register your models here.


class ModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Model, ModelAdmin)
