from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from webapp.models import Product


class ProductIndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
