from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.urls import reverse

User = get_user_model()


class Product(models.Model):
    CATEGORY_CHOICES = [('other', 'Разное'), ('drinks', 'Напитки'), ('food', 'Еда'),
                        ('books', 'Книги'), ('clothes', 'Одежда')]

    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, default=None,
                                   verbose_name='Описание')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other',
                                verbose_name='Категория')
    image = models.ImageField(null=True, blank=True, upload_to='products/', verbose_name='Картинка')

    def get_avg_rate(self):
        return self.reviews.all().filter(is_moderated=True).aggregate(avg=Avg('rate'))

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Продукт')
    text = models.TextField(max_length=3000, verbose_name='Текст отзыва')
    rate = models.PositiveIntegerField(verbose_name='Оценка', validators=(MinValueValidator(1), MaxValueValidator(5)))
    is_moderated = models.BooleanField(default=False, verbose_name='Отмодерировано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.author}, {self.product}, {self.is_moderated}"

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

        permissions = [
            ('change_review_status', 'Может изменять статус отзывов')
        ]
