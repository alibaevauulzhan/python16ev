from django.urls import path
# from product.views import product_list, ProductListView
from product import views
# urlpatterns = [
    # path('products/', product_list, name='products_list'), # для функций
    # path('products/create/', ProductListView.as_view()), # для класс apiview
#     path('products/', views.ProductListCreateView.as_view()),
#     path('products/<int:pk>/', views.ProductDetailView.as_view())
# ]
#
# localhost:8000/api/v1/products/1/ - GET -> DETAIL object
#                                     PUT/PATCH -> Update object
#                                     DELETE -> Delate object