from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.AdminAccountList.as_view(), name='관리자 계정 리스트'),
    path('<int:pk>', views.AdminAccountDetail.as_view(), name='관리자 계정 상세 정보'),
    path('pwd/<int:pk>', views.InitPWD.as_view(), name='비번초기화'),
    path('pwd/change/', views.ChangePWD.as_view(), name='비번초기화'),
    path('login/', views.doLogin.as_view(), name='관리자 로그인'),
]
