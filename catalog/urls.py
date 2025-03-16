from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

#  Задаем пространство имен для всех маршрутов в этом файле
app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
