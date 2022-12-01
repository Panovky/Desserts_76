from django.contrib import admin

from catalog.models import Filling
from catalog.models import Category

# Register your models here.
admin.site.register(Filling)
admin.site.register(Category)
