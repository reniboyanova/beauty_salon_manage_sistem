from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from beauty_salon_manage_sistem.products.forms import AddProductForm
from beauty_salon_manage_sistem.products.models import AddProducts


class ProductDetailsView(LoginRequiredMixin, ListView):
    template_name = 'products/display_products.html'
    model = AddProducts
    paginate_by = 8


class AddProductView(LoginRequiredMixin, CreateView):
    template_name = 'products/add_products.html'
    form_class = AddProductForm
    success_url = reverse_lazy('add product')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = AddProducts
    success_url = reverse_lazy('detail product')

    template_name = "products/delete_product.html"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = AddProducts
    fields = ('grams', 'image_of_product', 'serial_number')
    template_name = 'products/edit_product.html'

    def get_success_url(self):
        return reverse_lazy('index page with profile')