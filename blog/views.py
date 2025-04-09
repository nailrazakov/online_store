from blog.models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#  контроллер для отображения списка продуктов
class BlogListView(ListView):
    extra_context = {
        "title": "Статьи",
        "title_text": "Интересные статьи",
    }
    model = Blog


#  контроллер для отображения детальной информации о продукте
class BlogDetailView(DetailView):
    model = Blog


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


#  контроллер для удаления продукта
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
