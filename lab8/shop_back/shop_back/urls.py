from django.contrib import admin
from django.urls import path
from api.views import (ProductList, ProductDetail, 
                       CategoryList, CategoryDetail, 
                       CategoryProductsList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductList.as_view()),
    path('api/products/<int:pk>/', ProductDetail.as_view()),
    path('api/categories/', CategoryList.as_view()),
    path('api/categories/<int:pk>/', CategoryDetail.as_view()),
    path('api/categories/<int:id>/products/', CategoryProductsList.as_view()),
]