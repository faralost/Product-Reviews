from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(CreateView):
    form_class = ReviewForm
    template_name = 'review/create.html'
    model = Review

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_review'
    form_class = ReviewForm
    model = Review
    template_name = 'review/update.html'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_review'
    model = Review
    template_name = 'review/delete.html'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.product.pk})


class NotModeratedReviewsView(PermissionRequiredMixin, ListView):
    permission_required = 'webapp.change_review_status'
    model = Review
    context_object_name = 'reviews'
    template_name = 'review/not_moderated_reviews.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_moderated=False).order_by('-created_at')
