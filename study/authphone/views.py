import random

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AuthPhone
from .serializers import AuthPhoneCreateSerializer, AuthPhoneIsSuccessUpdateSerializer


# 인증 정보 저장
@api_view(['POST'])
def set_auth_info(request):
    temp_dict = request.data.copy()
    temp_dict['auth_number'] = random.randrange(100000, 999999)

    serializer = AuthPhoneCreateSerializer(data=temp_dict)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 인증 정보 변경
@api_view(['PUT'])
def update_auth_info(request, auth_phone_id):
    auth_info = get_object_or_404(AuthPhone, seq=auth_phone_id)
    serializer = AuthPhoneIsSuccessUpdateSerializer(auth_info,
                                                    data={'is_success': '0' if auth_info.is_success else '1',
                                                          'auth_number':
                                                              random.randrange(100000, 999999)
                                                              if auth_info.is_success else
                                                              auth_info.auth_number})
    if serializer.is_valid():
        serializer.save()
    return Response(status=status.HTTP_200_OK)
