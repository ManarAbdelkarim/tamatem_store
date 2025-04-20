from django.urls import path
from .views import ProductListAPIView, PurchaseAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/buy/', PurchaseAPIView.as_view(), name='product-buy'),

]
