from rest_framework.serializers import *

from .models import AuthPhone


class AuthPhoneSerializer(ModelSerializer):
    class Meta:
        model = AuthPhone
        fields = '__all__'


class AuthPhoneCreateSerializer(ModelSerializer):
    class Meta:
        model = AuthPhone
        fields = ('phone', 'auth_number')


class AuthPhoneIsSuccessUpdateSerializer(ModelSerializer):
    class Meta:
        model = AuthPhone
        fields = ('is_success',)