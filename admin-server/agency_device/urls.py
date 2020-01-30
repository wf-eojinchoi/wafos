from django.urls import path, re_path
from . import views


urlpatterns = [
    # path('', views.AgencyDeviceInfoList.as_view(), name='agency-device-info-list'),
    path('<int:pk>', views.AgencyDeviceInfoList.as_view(), name='agency-device-info-detail'),
    path('delete/<int:pk>', views.AgencyDeviceInfoDelete.as_view(), name='agency-device-info-delete'),
    path('ctrl_id/<int:pk>', views.ControllerIdList.as_view(), name='agency-device-info-detail'),
    # KIOSK LEVEL
    path('all/<int:pk>', views.AgencyDeviceInfoAllList.as_view(), name='agency-device-info-detail'),
    path('allow_ctrl_id/<int:agency>', views.AllowControlIdList.as_view(), name='agency-device-info-detail')

]
