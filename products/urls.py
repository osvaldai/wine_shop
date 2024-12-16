# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_detail, name='product_detail'),  # Главная страница с продуктом
    path('buy/', views.buy_product, name='buy_product'),  # Новый маршрут для покупки
    path('process_purchase/', views.process_purchase, name='process_purchase'),
    path('purchase_success/', views.purchase_success, name='purchase_success'),
]
