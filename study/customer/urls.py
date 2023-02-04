from django.urls import path

from . import views

urlpatterns = [
    path('signin/', views.signin),  # 회원 가입
    path('signup/', views.signup),  # 로그인
    path('info/', views.info),  # 내 정보 보기
    path('password/', views.password),  # 비밀번호 찾기(재설정)
]
