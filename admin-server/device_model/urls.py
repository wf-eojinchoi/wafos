from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.ModelList.as_view(), name='Model-list'),
    path('<int:pk>', views.ModelDetail.as_view(), name="Model-detail"),
]
