from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup),  # 회원 가입
    path('signin/', views.signin),  # 로그인
    path('mypage/<int:customer_id>', views.mypage),  # 내 정보 보기
    path('password/<int:auth_phone_id>', views.password),  # 비밀번호 찾기(재설정)
]
