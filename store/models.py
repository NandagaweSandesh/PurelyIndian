from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    highlights = models.TextField(blank=True)  # Added for highlights
    ingredients = models.TextField(blank=True)  # Added for ingredients
    nutritional_information = models.TextField(blank=True)  # Added for nutritional information
    storage_instructions = models.TextField(blank=True)  # Added for storage instructions
    shipping_and_delivery = models.TextField(blank=True)  # Added for shipping and delivery details
    how_to_enjoy = models.TextField(blank=True)  # Added for how to enjoy section
    why_choose_us = models.TextField(blank=True)  # Added for why choose us section
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name