from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product, ProductReview
from product.serializers import ProductSerializer, ProductCreateSerializer, ProductReviewSerializer

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

# 127.0.0.1:8000/api/v1/products/

# 1. Подход с созданием функции
# @api_view(['GET'])
# def product_list(request):
#     """
#     Функция для получения всех продуктов
#     :param request:
#     :return:
#     """
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
# # 2. Создание класса от APIView
# class ProductListView(APIView):
#     """
#     создание продукта
#     """
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = ProductCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 3. Generic APIView(
#     CRUD
#     CRUD - POST, GET, PUT/PATCH, DELETE
#     Create -> POST
#     Read -> GET
#     Update -> PUT/PATCH
#     Delete -> DELETE
#     )
#
# class ProductListCreateView(generics.ListCreateAPIView):
#     "Get метод"
#     queryset = Product.objects.all()
#     serializer_class = ProductCreateSerializer
# post, get -> ProductCreateSerializer
# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# put, get, delete -> ProductSerializer

# 4. ModelViewSet(
#     Create, Update, Delete, Retrieve
# )
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    # serializer = ProductCreateSerializer
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return ProductCreateSerializer
        return ProductSerializer
class ProductReviewViewSet(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer