from django.contrib import admin
from .models import User, ProductModel

# Register your models here.
admin.site.register(User),
admin.site.register(ProductModel)