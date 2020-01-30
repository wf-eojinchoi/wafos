from django.urls import path, re_path
from . import views


urlpatterns = [
    # path('', views.AgencyDeviceInfoList.as_view(), name='agency-device-info-list'),
    path('agency/<int:pk>', views.AgencyCourseList.as_view(), name='agency-course '),
    #<int:pk> 타입형이 int이고, pk라는 이름으로 값으로 받을거다.
    path('standard/<int:pk>', views.StandardCourseList.as_view(), name='standard-course '),
    #페이징처리를위한 새 uri
    path('standard/', views.StandardCourseList.as_view(), name='standard-course '),
    path('standard/copy/', views.StandardCourseCopy.as_view(), name='standard-course-copy '),
]
