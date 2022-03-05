from django.urls import path

from webapp.views.product import (ProductIndexView,
                                  ProductDetailView,
                                  ProductCreateView,
                                  ProductUpdateView,
                                  ProductDeleteView,)
from webapp.views.review import (ReviewCreateView,
                                 ReviewUpdateView,
                                 ReviewDeleteView,
                                 NotModeratedReviewsView,)

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('project/<int:pk>/add-review/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('reviews/not-moderated', NotModeratedReviewsView.as_view(), name='not_moderated_reviews')
]
