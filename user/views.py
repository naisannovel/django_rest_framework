from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


@api_view(['POST'])
def login(request):
    serializer = UserSerializer(data=request.data)
    # Using Raise exception
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('ok', status=status.HTTP_200_OK)

    # Using if else
    # if serializer.is_valid():
    #     return Response('ok', status=status.HTTP_200_OK)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


