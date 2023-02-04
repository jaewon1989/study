from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def signin(request):
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def signup(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def info(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def password(request):
    return Response(status=status.HTTP_200_OK)
