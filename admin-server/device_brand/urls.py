from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.BrandList.as_view(), name='Brand-list'),
    path('<int:pk>', views.BrandDetail.as_view(), name="Brand-detail"),
]
