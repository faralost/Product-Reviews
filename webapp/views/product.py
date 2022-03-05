from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductIndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
