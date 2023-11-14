from django.urls import path
from .views import new_category, category_list


urlpatterns = [
    path('', category_list, name='category_list'),
    path('new/', new_category, name='new_category'),
    ]
