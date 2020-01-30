from django.contrib import admin
from .models import CourseInfo

# Register your models here.


class CourseInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseInfo, CourseInfoAdmin)
