# coding=utf-8

from django.contrib import admin

from .models import Product, Category, ProductImages


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class ProductImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']
    inlines = [ProductImagesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
