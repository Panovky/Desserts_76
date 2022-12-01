from django.shortcuts import render
from django.views import generic
from catalog.models import Filling, Category


# Create your views here.
class FillingsView(generic.ListView):
    model = Filling
    context_object_name = 'fillings'


class CategoriesView(generic.ListView):
    model = Category
    context_object_name = 'categories'

