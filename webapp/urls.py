from django.urls import path

from webapp.views.product import ProductIndexView, ProductDetailView, ProductCreateView

app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
]