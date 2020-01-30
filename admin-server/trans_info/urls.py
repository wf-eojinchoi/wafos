from django.urls import path, re_path

from trans_info import views

urlpatterns = [
    path('', views.TransList.as_view(), name='Trans-list'),
    path('<int:pk>', views.TransDetail.as_view(), name="Trans-detail"),
    path('copy/', views.TCopy.as_view(), name="Trans-detail"),
]
