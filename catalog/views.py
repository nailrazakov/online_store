from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category


#  контроллер для отображения домашней страницы
def home(requests):
    #  возвращает все продукты
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(requests, "catalog/home.html", context)


#  контроллер для отображения страницы с контактной информацией.
def contacts(requests):
    if requests.method == "POST":
        name = requests.POST.get("name")
        phone = requests.POST.get("phone")
        message = requests.POST.get("message")
        print(name, phone, message)
        return HttpResponse(f"Спасибо, {name}! Данные успешно отправлены")
    return render(requests, "catalog/contacts.html")


#  контроллер вывода детальной информации о продукте по ключу
def product_detail(requests, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(requests, 'catalog/product_detail.html', context)
