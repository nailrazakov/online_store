from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category


#  контроллер для отображения домашней страницы
def home(requests):
    #  выводит в консоль последние 5 имен объектов
    list_of_products = Product.objects.all()[:5]
    for product in list_of_products:
        print(product.name)

    return render(requests, "catalog/home.html")


#  контроллер для отображения страницы с контактной информацией.
def contacts(requests):
    if requests.method == "POST":
        name = requests.POST.get("name")
        phone = requests.POST.get("phone")
        message = requests.POST.get("message")
        print(name, phone, message)
        return HttpResponse(f"Спасибо, {name}! Данные успешно отправлены")
    return render(requests, "catalog/contacts.html")
