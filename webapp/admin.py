from django.contrib import admin

from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['category']
    fields = ['name', 'description', 'category', 'image']
    list_display_links = ['id', 'name']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'rate', 'is_moderated']
    list_editable = ['is_moderated']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
