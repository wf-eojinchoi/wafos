from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.AgencyAccountList.as_view(), name='가맹점 계정 리스트'),
    path('<int:pk>', views.AgencyAccountDetail.as_view(), name='가맹점 계정 상세 정보'),
    path('pwd/init/', views.AgencyAccountInitPwd.as_view(), name='가맹점 계정 비밀번호 초기화'),
    path('pwd/change/', views.AgencyAccountChangePwd.as_view(), name='가맹점 계정 비밀번호 초기화'),
    path('login/', views.doLogin.as_view(), name='로그인'),
]
