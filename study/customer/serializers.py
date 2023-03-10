from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Customer
from .utils import check_auth_info


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerSignupSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('email', 'nickname', 'password', 'name', 'phone')

    def validate(self, data):
        check_auth_info(data['phone'])
        return data


class CustomerSigninpSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    nickname = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    def validate(self, data):

        if 1 == len(data):
            raise serializers.ValidationError('식별 가능한 정보를 최소 2개 이상 입력하세요.')
        if 2 == len(data) and ('name' in data):
            raise serializers.ValidationError('이름만으로는 로그인 할 수 없습니다.')

        q = Q()
        for key in data.keys():
            q.add(Q(**{key: data[key]}), q.AND)

        customer_info = Customer.objects.filter(q)
        if not customer_info.exists():
            raise serializers.ValidationError('로그인 정보가 없습니다.')

        return data


class CustomerInfoSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('email', 'nickname', 'name', 'phone')


class CustomerPasswordUpdateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('password', 'phone')

    def validate(self, data):
        check_auth_info(data['phone'])
        return data
