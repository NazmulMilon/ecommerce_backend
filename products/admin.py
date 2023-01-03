from django.contrib import admin
from .models import Category, Product, Brand


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # exclude = ['created_at', 'updated_at']
    list_display = ['product_category']


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['product_brand']


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'brand', 'product_description', 'brand', 'product_quantity',
                    'product_price', 'product_availability']
    # exclude = ['created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
