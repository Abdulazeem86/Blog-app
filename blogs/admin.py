from django.contrib import admin
from .models import User, ProductModel, ItemModel,CategoryModel

# Register your models here.
admin.site.register(User),
admin.site.register(ProductModel),
admin.site.register(ItemModel),
admin.site.register(CategoryModel),