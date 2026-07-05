from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name_cat = models.CharField('Название категории', max_length=100)
    description_cat = models.TextField('Описание категории')
    image_cat = models.ImageField('Изображение категории', upload_to='category/')
    slug_cat = models.SlugField('URL', unique=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug_cat:
            self.slug_cat = slugify(self.name_cat)  # было self.slug — исправил!
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_cat

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created']


class Country(models.Model):
    name = models.CharField('Название тура', max_length=100)
    description = models.TextField('Описание тура')
    price = models.PositiveIntegerField('Цена (₽)')
    image = models.ImageField('Главное изображение', upload_to='countries/')
    slug = models.SlugField('URL', unique=True)

    cat = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='countries',
    )

    # ДОПОЛНИТЕЛЬНЫЕ ПОЛЯ (рекомендую добавить)
    hotel = models.CharField('Отель', max_length=200, blank=True)
    stars = models.IntegerField('Звёздность отеля', choices=[(i, f'{i}★') for i in range(1, 6)], default=3)
    nights = models.IntegerField('Количество ночей', default=7)
    meal = models.CharField('Питание', max_length=50, default='BB', choices=[
        ('BB', 'Завтраки'),
        ('HB', 'Завтрак + ужин'),
        ('FB', '3-разовое питание'),
        ('AI', 'Всё включено'),
    ])
    transfer = models.BooleanField('Трансфер включён', default=True)
    insurance = models.BooleanField('Медицинская страховка', default=True)

    # Даты
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.nights} ночей)'

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ['-created']


class Review(models.Model):
    tour = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    text = models.TextField('Текст отзыва')
    rating = models.IntegerField('Оценка', choices=[(i, f'{i}★') for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.tour.name} - {self.rating}★'