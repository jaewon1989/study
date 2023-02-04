from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AuthPhone
from .serializers import AuthPhoneSerializer


# 전화번호 인증 저장
@api_view(['POST'])
def setAuthInfo(request):
    serializer = AuthPhoneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 전화번호 인증 여부 확인
@api_view(['GET'])
def getAuthInfoByPhone(request, phone):
    authInfo = get_object_or_404(AuthPhone, phone=phone)
    serializer = AuthPhoneSerializer(authInfo)
    return Response(serializer.data.get('is_success'), status=status.HTTP_200_OK)
