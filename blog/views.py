from blog.models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


#  контроллер для отображения списка продуктов
class BlogListView(ListView):
    extra_context = {
        "title": "Статьи",
        "title_text": "Интересные статьи",
    }
    model = Blog

    #  Фильтрация опубликованных статей: выводить в список статей только те, которые имеют положительный признак публикации.
    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


#  контроллер для отображения детальной информации о продукте
class BlogDetailView(DetailView):
    model = Blog

    #  Увеличение счетчика просмотров: при открытии отдельной статьи увеличивает счетчик просмотров.
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_counter += 1
        obj.save()
        return obj


#  контроллер для создания продукта
class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published", "view_counter")
    success_url = reverse_lazy("blog:blog_list")


#  контроллер для изменения продукта
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published", "view_counter")
    success_url = reverse_lazy("blog:blog_list")

    #  Перенаправление после редактирования: после успешного редактирования записи перенаправлет пользователя
    #  на просмотр этой статьи.
    def get_success_url(self):
        print('Работает')
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


#  контроллер для удаления продукта
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
