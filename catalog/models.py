from django.db import models


class Category(models.Model):
    """Класс для модели категория"""

    name = models.CharField(
        max_length=255,
        verbose_name="Название категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="media/",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    #  дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    #  дата последнего изменения
    updated_at = models.DateTimeField(auto_now=True)
    #  статус публикации
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]
