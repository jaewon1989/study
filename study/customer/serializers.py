from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import *

from .models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerCreateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('email', 'nick_name', 'password', 'name', 'phone')


class CustomerSignUpSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    nick_name = serializers.CharField(required=False)
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

        customerInfo = Customer.objects.filter(q)
        if not customerInfo.exists():
            raise serializers.ValidationError('로그인 정보가 없습니다.')

        return True


class CustomerInfoSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('email', 'nick_name', 'name', 'phone', 'create_dt')


class CustomerPasswordUpdateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('password',)
