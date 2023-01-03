from django.db import models


# Create your models here.

class Category(models.Model):
    product_category = models.CharField(max_length=100, help_text='category name')
    created_at = models.DateField(auto_now_add=True, help_text='created time of category')
    updated_at = models.DateField(auto_now=True, help_text='category name updated time')

    class Meta:
        db_table = 'categories'


class Brand(models.Model):
    product_brand = models.CharField(max_length=100, help_text='Product brand name')

    class Meta:
        db_table = 'brands'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Product Category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, help_text='Product Brand')
    product_name = models.CharField(max_length=100, help_text='name of product')
    product_description = models.TextField(blank=True)
    product_quantity = models.IntegerField(blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_availability = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, help_text='Product created time')
    updated_at = models.DateField(auto_now=True, help_text='Product updated time')

    class Meta:
        db_table = 'products'
