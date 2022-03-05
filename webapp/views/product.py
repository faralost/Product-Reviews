from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product, Review


class ProductIndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all().filter(is_moderated=True)
        context['avg'] = self.get_avg_rate()
        return context

    def get_avg_rate(self):
        avg = self.object.reviews.all().filter(is_moderated=True).aggregate(avg=Avg('rate'))
        return avg


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_product'
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_product'
    model = Product
    form_class = ProductForm
    template_name = 'product/update.html'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_product'
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
