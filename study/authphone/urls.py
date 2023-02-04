from django.urls import path

from . import views

urlpatterns = [
    path('', views.setAuthInfo),  # 인증 정보 저장
    path('<str:phone>', views.updateAuthInfoByPhone),  # 인증 정보 변경
    path('check/<str:phone>', views.getAuthInfoByPhone),  # 인증 유무 확인
]
