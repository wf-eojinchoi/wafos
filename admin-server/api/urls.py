from django.urls import path, re_path, include

from api import common_fileupload_views, audio_fileupload_views, wf_migrate, update_fileupload_views
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # KIOSK LEVEL
    path('wafos/', include('wafos.urls')),

    # ADMIN LEVEL
    path('member/', include('member.urls')),
    path('account/agency/', include('agency_account.urls')),
    path('agency/', include('agency.urls')),
    path('agency/device/', include('agency_device.urls')),
    path('course_info/', include('course_info.urls')),
    path('device/brand/', include('device_brand.urls')),
    path('device/model/', include('device_model.urls')),
    path('device/info/', include('device_info.urls')),
    path('device/etc/', include('etc_device.urls')),
    path('payment/', include('payment.urls')),
    path('admin/', include('admin_account.urls')),
    path('trans/', include('trans_info.urls')),
    path('tubelink/', views.TubeLink.as_view(), name='광고링크설정'),
    path('migrate/<int:sid>', wf_migrate.WFMigrate.as_view(), name='마이그레이션'),
    path('migrate/user/<int:sid>', wf_migrate.WFMigrateUser.as_view(), name='마이그레이션'),
    path('migrate/pay/<int:sid>', wf_migrate.WFMigratePay.as_view(), name='마이그레이션'),
    path('migrate/device/<int:sid>', wf_migrate.WFMigrateDevice.as_view(), name='마이그레이션'),
    path('migrate/course/<int:sid>', wf_migrate.WFMigrateCourse.as_view(), name='마이그레이션'),
    path('common/file/', common_fileupload_views.FileUploadView.as_view(), name='file_upalod'),
    path('common/file/audio/', audio_fileupload_views.FileUploadView.as_view(), name='audio file_upalod'),
    path('common/file/update/', update_fileupload_views.FileUploadView.as_view(), name='update file_upalod'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token-refresh',
         TokenRefreshView.as_view(), name='token_refresh'),
]
