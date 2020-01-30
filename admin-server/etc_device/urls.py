from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.EtcDeviceList.as_view(), name='EtcDevice-list'),
    path('<int:pk>', views.EtcDeviceDetail.as_view(), name="EtcDevice-detail"),
]
