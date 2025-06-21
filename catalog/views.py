from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from catalog.services import show_categories


#  контроллер для отображения списка продуктов
class ProductListView(ListView):
    extra_context = {
        "title": "Домашняя",
        "title_text": "На нашем сайте возможно заказать электронные средства",
        "category": show_categories(),
    }
    model = Product

    #  template_name = 'app_name/model_list.html'
    #  context_object_name = object_list
    #  Фильтрация опубликованных продуктов: выводить только те, которые имеют положительный признак публикации.
    #  А для пользователей которые имеют право на смену признака публикации показывает все товары

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return queryset
        else:
            return queryset.filter(is_published=True)


#  контроллер для отображения детальной информации о продукте
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    #  template_name = 'app_name/model_detail.html'
    context_object_name = "product"


#  контроллер для создания продукта
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


#  контроллер для изменения продукта
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        elif self.request.user.has_perm('catalog.can_unpublish_product'):
            return self.object
        raise PermissionDenied

    def form_valid(self, form):
        """
        Проверка прав доступа к изменению поля объекта
        """
        obj = self.get_object()
        new_is_published = form.cleaned_data.get('is_published')
        if obj.is_published is True and new_is_published is False:
            if not self.request.user.has_perm('catalog.can_unpublish_product'):
                return HttpResponseForbidden('У Вас нет права снимать с публикации')
        return super().form_valid(form)


#  контроллер для удаления продукта
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    #  удалять могут те пользователи у которых есть разрешения
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        elif self.request.user.has_perm('catalog.delete_product'):
            return self.object
        raise PermissionDenied


#  контроллер для отображения страницы с контактной информацией.
class ContactsView(View):
    extra_context = {
        "title": "Контакты",
    }
    template_name = 'catalog/contacts.html'

    def get(self, request):
        print(f'Вызов страницы с контактами')
        return render(request, template_name=self.template_name)

    def post(self, request):
        name = self.request.POST.get('name')
        phone = self.request.POST.get('phone')
        message = self.request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
        return render(request, template_name=self.template_name)


class ProductInCategoryListView(ProductListView):
    template_name = 'catalog/product_in_category.html'
    extra_context = {
        "category": show_categories(),
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        cat = self.kwargs.get('pk')
        return queryset.filter(category_id=cat)

    #  для отображения оглавления страницы
    def get_context_data(self, **kwargs):
        cat = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['cat'] = show_categories(cat)
        return context
