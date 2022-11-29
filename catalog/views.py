from django.shortcuts import render
from django.views import generic
from catalog.models import Filling


# Create your views here.
class FillingsView(generic.ListView):
    model = Filling
    context_object_name = 'fillings'