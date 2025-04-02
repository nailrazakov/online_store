from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category


#  контроллер для отображения домашней страницы
def home(requests):
    #  возвращает все продукты
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Домашняя',
        'title_text': 'На нашем сайте возможно заказать электронные средства'
    }
    return render(requests, "catalog/home.html", context)


#  контроллер для отображения страницы с контактной информацией.
def contacts(requests):
    context = {
        'title': 'Контакты',
    }
    if requests.method == "POST":
        name = requests.POST.get("name")
        phone = requests.POST.get("phone")
        message = requests.POST.get("message")
        print(name, phone, message)
        return HttpResponse(f"Спасибо, {name}! Данные успешно отправлены")
    return render(requests, "catalog/contacts.html", context)


#  контроллер вывода детальной информации о продукте по ключу
def product_detail(requests, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(requests, 'catalog/product_detail.html', context)


def create(requests):
    context = {
        'message': 'Введите данные'
    }
    if requests.method == "POST":
        name = requests.POST.get("name")
        description = requests.POST.get("description")
        price = requests.POST.get("price")
        try:
            product = Product(name=name, description=description, price=price)
            product.save()
            context = {
                'message': "Продукт записан"
            }
        except:
            context = {
                'message': "Проверьте данные"
            }

    return render(requests, "catalog/create.html", context)
