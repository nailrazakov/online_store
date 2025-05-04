from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


#  контроллер для отображения списка продуктов
class ProductListView(ListView):
    extra_context = {
        "title": "Домашняя",
        "title_text": "На нашем сайте возможно заказать электронные средства",
    }
    model = Product
    #  template_name = 'app_name/model_list.html'
    #  context_object_name = object_list


#  контроллер для отображения детальной информации о продукте
class ProductDetailView(DetailView):
    model = Product
    #  template_name = 'app_name/model_detail.html'
    context_object_name = "product"


#  контроллер для создания продукта
class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:product_list")


#  контроллер для изменения продукта
class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:product_list")


#  контроллер для удаления продукта
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


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
