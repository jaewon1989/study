from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSignInSerializer, CustomerSignUpSerializer, CustomerInfoSerializer, \
    CustomerPasswordUpdateSerializer


# 회원 가입
@api_view(['POST'])
def signin(request):
    serializer = CustomerSignInSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인
@api_view(['POST'])
def signup(request):
    serializer = CustomerSignUpSerializer(data=request.data)
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
def password(request, customer_id):
    customer_info = get_object_or_404(Customer, seq=customer_id)
    serializer = CustomerPasswordUpdateSerializer(customer_info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
