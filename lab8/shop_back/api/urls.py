from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', views.product_detail),
    path('categories/', views.category_list),
    path('categories/<int:id>/', views.category_detail),
    path('categories/<int:id>/products/', views.products_by_category),
]
