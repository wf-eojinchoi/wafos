from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # KIOSK AGENCY LEVEL
    # 가맹점 정보 보기 GET : /api/agency/'가맹점 ID'
    # 가맹점 장비 보기 GET : /api/agency/device/all/'가맹점 ID'?type=0
    #                   | type 모델 정보
    #                   | type = models.IntegerField(
    #                   |     verbose_name='타입',
    #                   |     choices=(
    #                   |         (0, '세탁기'),
    #                   |         (1, '건조기'),
    #                   |         (2, '트롬스타일러')
    #                   |         (3, '세탁용품')
    #                   |     ))
    # 가맹점 장비 - 코스 보기 GET : /api/course_info/agency/'가맹점 장비 ID(가맹점 장비 보기 object id'
    # 기타 장비의 Course 정보 확인 하기 : 고정 코스 장비가 있는듯 함. (업체 확인해보고 적용)


    # KIOSK -- polling API
    # 원격으로 코인신호보내기(제거) < 너무 위험
    # 냉난방기 ON/OFF API :
    # 서비스 점검 팝업 API :
    # 광고이미지 API :
    # 경고 방송 정보 API :
    # PC 재부팅 API : 가능?
    # 프로그램 재시작 : 필요한가?


    # KIOSK LOG : 확정 아님 추후 유지보수용으로 쓸까 말까 고민중
    # 코인 보낸 횟수 LOG POST : /api/wafos/log/coin/
    # 지폐인식기 받을때 마다 LOG POST : /api/wafos/log/money/

    # KIOSK USER LEVEL
    path('login', views.MemberLogin.as_view(), name='회원 로그인'),
    path('signup', views.MemberSignUp.as_view(), name='회원 가입'),
    path('init-check', views.AgencyInitCheck.as_view(), name='초기 확인'),
    path('point', views.AgencyPointInfo.as_view(), name="agency-point-info"),
    path('agency-account/<str:login_id>',
         views.AgencyAccountDetail.as_view(), name='가맹점 계정 상세 정보'),
    path('agency-devices', views.AgencyDeviceInfoAllList.as_view(),
         name='agency-device-info-all-list'),
    path('agency-courses', views.AgencyCourseList.as_view(),
         name='agency-course-list'),
    # 결제 정보 전송
    # 지폐,카드 입력 전송
    path('payment', views.AgencyPayment.as_view(), name='회원 가입'),

    # 경고 방송
    path('alert', views.AlertInfoViews.as_view(), name='회원 가입'),
    path('tubelink', views.TubeLinkViews.as_view(), name='튜브링크'),
    path('payment-member/<int:user>', views.AgencyMemberPayment.as_view(),
         name="Payment-detail")
]
