from django.contrib import admin

from catalog.models import Filling
from catalog.models import Category
from catalog.models import Dessert

admin.site.register(Filling)
admin.site.register(Category)
admin.site.register(Dessert)
