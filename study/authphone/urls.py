from django.urls import path

from . import views

urlpatterns = [
    path('', views.set_auth_info),  # 인증 정보 저장
    path('<int:auth_phone_id>', views.update_auth_info),  # 인증 정보 변경
]
