from catalog.models import Category, Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def show_categories(category_id=None):
    """
    Сервисная функция возвращает объекты Category, если передать значение вернет конкретный объект
    :param category_id: int
    :return: queryset or object
    """
    if category_id is not None:
        return Category.objects.get(pk=category_id)
    else:
        return Category.objects.all()


def get_products_from_cache():
    """
    Проверяет если кеширование включено то получает данные о продуктах из кеша если есть
    если нет записывает в кеш
    :return: Объекты Product, если есть то из кеша
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
