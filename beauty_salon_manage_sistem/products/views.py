from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from beauty_salon_manage_sistem.products.forms import AddProductForm
from beauty_salon_manage_sistem.products.models import AddProducts


class ProductDetailsView(ListView):
    template_name = 'products/display_products.html'
    model = AddProducts


class AddProductView(CreateView):
    template_name = 'products/add_products.html'
    form_class = AddProductForm
    success_url = reverse_lazy('add product')


class ProductDeleteView(DeleteView):
    model = AddProducts
    success_url = reverse_lazy('index page')

    template_name = "products/delete_product.html"
