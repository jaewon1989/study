from authphone.models import AuthPhone
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSignupSerializer, CustomerSigninpSerializer, CustomerInfoSerializer, \
    CustomerPasswordUpdateSerializer


# 회원 가입
@api_view(['POST'])
def signup(request):
    serializer = CustomerSignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인
@api_view(['POST'])
def signin(request):
    serializer = CustomerSigninpSerializer(data=request.data)
    if serializer.is_valid():
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 내 정보 보기
@api_view(['GET'])
def mypage(request, customer_id):
    customer_info = get_object_or_404(Customer, seq=customer_id)
    serializer = CustomerInfoSerializer(customer_info)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 비밀번호 찾기(재설정)
@api_view(['PUT'])
def password(request, auth_phone_id):
    auth_info = get_object_or_404(AuthPhone, seq=auth_phone_id)
    temp_dict = request.data.copy()
    temp_dict['phone'] = auth_info.phone

    customer_info = get_object_or_404(Customer, phone=auth_info.phone)
    serializer = CustomerPasswordUpdateSerializer(customer_info, data=temp_dict)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
