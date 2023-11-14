from django.urls import path, include
from .views import new_product, product_list, edit_product, delete_product


urlpatterns = [
    path('', product_list, name='product_list'),
    path('new/', new_product, name='new_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]
