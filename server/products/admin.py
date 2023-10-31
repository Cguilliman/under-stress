from django.contrib import admin
from .models import Product


admin.site.register(Product, list_display=("__str__", "author", "created_at"))

