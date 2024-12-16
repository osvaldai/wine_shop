from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


# Представление для главной страницы продукта
def product_detail(request):
    # Переход на главную страницу с продуктом (здесь нет привязки к базе данных)
    return render(request, 'index.html')


# Представление для оформления покупки
def buy_product(request):
    # Переход на страницу оформления данных пользователя
    return render(request, 'purchase.html')


# Представление для обработки оплаты (без проверки наличия товара в базе данных)
@require_POST
def process_purchase(request):
    # Получение данных пользователя
    name = request.POST.get('name')
    email = request.POST.get('email')
    quantity = request.POST.get('quantity')

    # Логика для последующей обработки заказа (например, отправка данных)
    # Пока без взаимодействия с базой данных

    # Перенаправляем на страницу с успешной оплатой
    return redirect('purchase_success')


# Представление для успешной покупки
def purchase_success(request):
    return render(request, 'success.html')
