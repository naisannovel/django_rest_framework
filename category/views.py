from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from .models import Category
from django.shortcuts import get_list_or_404


@api_view(['POST'])
def new_category(request):
    serializer = CategorySerializer(data=request.data)
    # Using Raise exception
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('Successfully category created', status=status.HTTP_200_OK)


@api_view(['GET'])
def category_list(request):
    categories = get_list_or_404(Category)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




