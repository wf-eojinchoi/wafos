from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.DeviceList.as_view(), name='Device-list'),
    path('<int:pk>', views.DeviceDetail.as_view(), name="Device-detail"),
]
