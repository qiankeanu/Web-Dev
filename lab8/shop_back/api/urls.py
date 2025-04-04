from django.http import HttpResponse
from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, ProductsByCategory

# Функция для отображения главной страницы
def home(request):
    return HttpResponse("Добро пожаловать в наш магазин!")

urlpatterns = [
    path("", home, name="home"),  # Маршрут для главной страницы
    path("products/", ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("categories/", CategoryList.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("categories/<int:id>/products/", ProductsByCategory.as_view(), name="category-products"),
]
