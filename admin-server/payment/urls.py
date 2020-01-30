from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.PaymentList.as_view(), name='Payment-list'),
    path('month/', views.PaymentMonthList.as_view(), name='Payment-list'),
    path('day/', views.PaymentDayList.as_view(), name='Payment-list'),
    path('year/', views.YearList.as_view(), name='Payment-list'),
    path('<int:pk>', views.PaymentDetail.as_view(), name="Payment-detail"),
    path('member/<int:agency>/<int:user>', views.AgencyMemberPayment.as_view(), name="Payment-detail"),
    path('download/', views.DnExcel.as_view(), name="agency-payment-dn"),
]
