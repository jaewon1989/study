from rest_framework.serializers import ModelSerializer

from .models import AuthPhone


class AuthPhoneSerializer(ModelSerializer):
    class Meta:
        model = AuthPhone
        fields = '__all__'
