from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# 인증 정보 저장
@api_view(['POST'])
def setAuthInfo(request):
    serializer = AuthPhoneCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 인증 정보 변경
@api_view(['PUT'])
def updateAuthInfoByPhone(request, phone):
    authPhoneInfo = get_object_or_404(AuthPhone, phone=phone)
    serializer = AuthPhoneIsSuccessUpdateSerializer(authPhoneInfo,
                                                    data={'is_success': '0' if authPhoneInfo.is_success else '1'})
    if serializer.is_valid():
        serializer.save()
    return Response(status=status.HTTP_200_OK)


# 인증 유무 확인
@api_view(['GET'])
def getAuthInfoByPhone(request, phone):
    authPhoneInfo = get_object_or_404(AuthPhone, phone=phone)
    serializer = AuthPhoneSerializer(authPhoneInfo)
    if serializer.data.get('is_success'):
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_403_FORBIDDEN)
