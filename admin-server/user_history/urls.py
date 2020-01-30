from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.UserHistoryList.as_view(), name='회원 사용 내역'),
    path('<int:pk>', views.UserHistoryDetail.as_view(), name="회원 사용내역 상세"),
]
