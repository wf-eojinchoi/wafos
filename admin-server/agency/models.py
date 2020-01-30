from django.db import models

# Create your models here.


class Agency(models.Model):
    agency_code = models.CharField(
        max_length=256,
        verbose_name='대리점 코드')
    zipcode = models.CharField(
        null=True, blank=True,
        max_length=12,
        verbose_name='우편번호')
    addr1 = models.CharField(
        null=True, blank=True,
        max_length=128,
        verbose_name='기본주소')
    addr2 = models.CharField(
        null=True, blank=True,
        max_length=128,
        verbose_name='상세주소')
    tel = models.CharField(
        null=True, blank=True,
        max_length=11,
        verbose_name='대리점 전화번호')
    phone = models.CharField(
        null=True, blank=True,
        max_length=11,
        verbose_name='점주 휴대폰')
    ip_addr = models.CharField(
        default=None, null=True, blank=True,
        max_length=15,
        verbose_name='ip 주소')
    agency_owner = models.CharField(
        null=True, blank=True,
        max_length=256,
        verbose_name='점주이름')
    agency_name = models.CharField(
        null=True, blank=True,
        max_length=100,
        verbose_name='지점명')
    cor_number = models.CharField(
        default=None, null=True, blank=True,
        max_length=100,
        verbose_name='사업자번호')
    memo = models.TextField(
        default=None, null=True, blank=True,
        verbose_name='비고')
    expire_date = models.DateField(
        default=None, null=True, blank=True,
        verbose_name='유지보수 만료일')
    upd_dttm = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='가입일')

    # 키오스크 메뉴 권한정보
    menu_wash = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 세탁'
    )
    menu_dry = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 건조'
    )
    menu_shoes_wash = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 운동화세탁'
    )
    menu_shoes_dry = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 운동화건조'
    )
    menu_point = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 현금적립'
    )
    menu_air = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 냉난방'
    )
    menu_tromm = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 트롬스타일러'
    )
    menu_item = models.BooleanField(
        default=False,
        verbose_name='메뉴 - 세탁용품'
    )
    menu_card = models.BooleanField(
        default=False,
        verbose_name='카드단말기 사용여부'
    )
    menu_signup = models.BooleanField(
        default=False,
        verbose_name='회원/비회원 사용여부'
    )
    menu_lang_ko = models.BooleanField(
        default=True,
        verbose_name='한글 메뉴 사용여부'
    )
    menu_lang_en = models.BooleanField(
        default=True,
        verbose_name='영어 메뉴 사용여부'
    )
    menu_lang_vn = models.BooleanField(
        default=False,
        verbose_name='베트남어 메뉴 사용여부'
    )

    class Meta:
        db_table = 'agency'
        verbose_name = '대리점 정보'


class AgencyPoint(models.Model):
    agency = models.ForeignKey(
        Agency,
        on_delete=models.SET_NULL, null=True,
        blank=True,
        verbose_name='agency_id')
    use_point = models.IntegerField(
        default=0,
        verbose_name='사용가능 포인트'
    )
    # 기본 정보
    def_day_new = models.IntegerField(
        default=0,
        verbose_name='기본-주중 신규 포인트'
    )
    def_day_wash = models.IntegerField(
        default=0,
        verbose_name='기본-주중 세탁 포인트'
    )
    def_day_dry = models.IntegerField(
        default=0,
        verbose_name='기본-주중 건조 포인트'
    )
    def_day_shoes_wash = models.IntegerField(
        default=0,
        verbose_name='기본-주중 운동화세탁 포인트'
    )
    def_day_shoes_dry = models.IntegerField(
        default=0,
        verbose_name='기본-주중 운동화건조 포인트'
    )
    def_weekend_new = models.IntegerField(
        default=0,
        verbose_name='기본-주말 신규 포인트'
    )
    def_weekend_wash = models.IntegerField(
        default=0,
        verbose_name='기본-주말 세탁 포인트'
    )
    def_weekend_dry = models.IntegerField(
        default=0,
        verbose_name='기본-주말 건조 포인트'
    )
    def_weekend_shoes_wash = models.IntegerField(
        default=0,
        verbose_name='기본-주말 운동화세탁 포인트'
    )
    def_weekend_shoes_dry = models.IntegerField(
        default=0,
        verbose_name='기본-주말 운동화건조 포인트'
    )
    
    # 카드 기본 정보
    def_card_day_new = models.IntegerField(
        default=0,
        verbose_name='카드-주중 신규 포인트'
    )
    def_card_day_wash = models.IntegerField(
        default=0,
        verbose_name='카드-주중 세탁 포인트'
    )
    def_card_day_dry = models.IntegerField(
        default=0,
        verbose_name='카드-주중 건조 포인트'
    )
    def_card_day_shoes_wash = models.IntegerField(
        default=0,
        verbose_name='카드-주중 운동화세탁 포인트'
    )
    def_card_day_shoes_dry = models.IntegerField(
        default=0,
        verbose_name='카드-주중 운동화건조 포인트'
    )
    def_card_weekend_new = models.IntegerField(
        default=0,
        verbose_name='카드-주말 신규 포인트'
    )
    def_card_weekend_wash = models.IntegerField(
        default=0,
        verbose_name='카드-주말 세탁 포인트'
    )
    def_card_weekend_dry = models.IntegerField(
        default=0,
        verbose_name='카드-주말 건조 포인트'
    )
    def_card_weekend_shoes_wash = models.IntegerField(
        default=0,
        verbose_name='카드-주말 운동화세탁 포인트'
    )
    def_card_weekend_shoes_dry = models.IntegerField(
        default=0,
        verbose_name='카드-주말 운동화건조 포인트'
    )

    # 이벤트 정보
    evt_st_date = models.DateField(
        null=True,
        verbose_name='이벤트 시작일'
    )
    evt_et_date = models.DateField(
        null=True,
        verbose_name='이벤트 종료일'
    )
    evt_day_new = models.IntegerField(
        default=0,
        verbose_name='이벤트-주중 신규 포인트'
    )
    evt_day_wash = models.IntegerField(
        default=0,
        verbose_name='이벤트-주중 세탁 포인트'
    )
    evt_day_dry = models.IntegerField(
        default=0,
        verbose_name='이벤트-주중 건조 포인트'
    )
    evt_day_shoes_wash = models.IntegerField(
        default=0,
        verbose_name='이벤트-주중 운동화세탁 포인트'
    )
    evt_day_shoes_dry = models.IntegerField(
        default=0,
        verbose_name='이벤트-주중 운동화건조 포인트'
    )
    evt_weekend_new = models.IntegerField(
        default=0,
        verbose_name='이벤트-주말 신규 포인트'
    )
    evt_weekend_wash = models.IntegerField(
        default=0,
        verbose_name='이벤트-주말 세탁 포인트'
    )
    evt_weekend_dry = models.IntegerField(
        default=0,
        verbose_name='이벤트-주말 건조 포인트'
    )
    evt_weekend_shoes_wash = models.IntegerField(
        default=0,
        verbose_name='이벤트-주말 운동화세탁 포인트'
    )
    evt_weekend_shoes_dry = models.IntegerField(
        default=0,
        verbose_name='이벤트-주말 운동화건조 포인트'
    )
    upd_dttm = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일')
    reg_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='가입일')

    class Meta:
        db_table = 'agency_point'
        verbose_name = '대리점 적립금 정보'
