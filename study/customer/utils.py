from authphone.models import AuthPhone
from rest_framework import serializers


def check_auth_phone_info(phone):
    try:
        auth_phone_info = AuthPhone.objects.get(phone=phone)
    except AuthPhone.DoesNotExist:
        raise serializers.ValidationError('전화번호 인증 정보가 없습니다.')
    else:
        if not auth_phone_info.is_success:
            raise serializers.ValidationError('전화번호 인증이 유효하지 않습니다.')
