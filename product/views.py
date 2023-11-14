from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


@api_view(['POST'])
def new_product(request):
    serializer = ProductSerializer(data=request.data)
    # Using Raise exception
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'msg': 'Successfully Product created', 'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_list(request):
    products = get_list_or_404(Product)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

    # try:
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # except Product.DoesNotExist:
    #     return Response('Something went wrong', status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print('product', product)
    serializer = ProductSerializer(product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('Successfully Product updated', status=status.HTTP_200_OK)

    # try:
    #     product = Product.objects.get(pk=product_id)
    #     serializer = ProductSerializer(product, data=request.data)
    #     ''' instance=product  # if you want to update all fields then no need to pass instance
    #     if you want to update some fields then need to pass instance '''
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response('Successfully Product updated', status=status.HTTP_200_OK)
    # except Product.DoesNotExist:
    #     return Response('Something went wrong', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return Response('Successfully Product deleted', status=status.HTTP_200_OK)
