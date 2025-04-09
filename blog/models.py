from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(verbose_name='Изображение', upload_to="media/", blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True)
    view_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
