from catalog.models import Category


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
