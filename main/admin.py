from django.contrib import admin
from .models import Category, Country

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_cat', 'slug_cat', 'created']
    prepopulated_fields = {'slug_cat': ('name_cat',)}
    search_fields = ['name_cat']
    readonly_fields = ['created', 'updated']  # ← добавляем
    fieldsets = (
        ('Основное', {
            'fields': ('name_cat', 'description_cat', 'image_cat', 'slug_cat')
        }),
        ('Даты', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'cat', 'price', 'stars', 'nights', 'meal', 'transfer', 'insurance']
    list_filter = ['cat', 'stars', 'meal', 'transfer', 'insurance']
    search_fields = ['name', 'hotel']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stars', 'nights', 'meal', 'transfer', 'insurance']
    readonly_fields = ['created', 'updated']  # ← добавляем
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'description', 'price', 'image', 'slug', 'cat')
        }),
        ('Отель и питание', {
            'fields': ('hotel', 'stars', 'nights', 'meal')
        }),
        ('Услуги', {
            'fields': ('transfer', 'insurance')
        }),
        ('Даты', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'tour', 'rating', 'created_at']
    list_filter = ['rating', 'tour']
    search_fields = ['user__username', 'text']