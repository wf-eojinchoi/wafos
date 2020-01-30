from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.AgencyList.as_view(), name='agency-list'),
    path('all/', views.AgencyListAll.as_view(), name='agency-list'),
    path('<int:pk>', views.AgencyDetail.as_view(), name="agency-detail"),
    path('point/<int:pk>', views.AgencyPointInfo.as_view(), name="agency-detail"),
    path('alert/', views.AgencyAlertRegist.as_view(), name="agency-alert-reg"),
    path('update/all/', views.AgencyUpdateAll.as_view(), name="agency-update-all"),
]
