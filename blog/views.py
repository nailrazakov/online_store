from blog.models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin


#  from django.core.mail import send_mail

def send_mail():
    print('Статья очень популярна')


#  контроллер для отображения списка продуктов
class BlogListView(ListView):
    extra_context = {
        "title": "Статьи",
        "title_text": "Интересные статьи",
    }
    model = Blog

    #  Фильтрация опубликованных статей: выводить только те, которые имеют положительный признак публикации.
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
        if obj.view_counter > 100:
            send_mail()
        return obj


#  контроллер для создания продукта
class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published", "view_counter")
    success_url = reverse_lazy("blog:blog_list")
    permission_required = 'blog.add_blog'


#  контроллер для изменения продукта
class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published", "view_counter")
    success_url = reverse_lazy("blog:blog_list")
    permission_required = 'blog.change_blog'

    #  Перенаправление после редактирования: после успешного редактирования записи перенаправлет пользователя
    #  на просмотр этой статьи.
    def get_success_url(self):
        print('Работает')
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


#  контроллер для удаления продукта
class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
    permission_required = 'blog.delete_blog'
