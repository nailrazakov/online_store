from django.shortcuts import render
from django.http import HttpResponse


#  контроллер для отображения домашней страницы
def home(requests):
    return render(requests, 'catalog/home.html')


#  контроллер для отображения страницы с контактной информацией.
def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')
        print(name, phone, message)
        return HttpResponse(f'Спасибо, {name}! Данные успешно отправлены')
    return render(requests, 'catalog/contacts.html')
