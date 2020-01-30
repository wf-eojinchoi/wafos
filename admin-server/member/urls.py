from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.MemberList.as_view(), name='member-list'),
    path('<int:pk>', views.MemberDetail.as_view(), name="member-detail"),
    path('change/point/', views.MemberChangePoint.as_view(), name="member-change-point"),
    path('change/money/', views.MemberChangeMoney.as_view(), name="member-change-money"),
    path('change/memo/', views.MemberChangeMemo.as_view(), name="member-change-money"),
    path('change/pwd/', views.MemberInitPwd.as_view(), name="member-init-pwd"),
    path('agency/<int:pk>', views.AgencyMemberList.as_view(), name='agency-member-list'),
    path('agency/<int:pk>/<int:user>', views.AgencyMemberDetail.as_view(), name="agency-member-detail"),
    path('download/', views.DnExcel.as_view(), name="agency-member-dn"),
]
