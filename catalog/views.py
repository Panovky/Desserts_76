from django.shortcuts import render
from django.views import generic
from catalog.models import Filling, Category, Dessert


# Create your views here.
class FillingsView(generic.ListView):
    model = Filling
    context_object_name = 'fillings'


class CategoriesView(generic.ListView):
    model = Category
    context_object_name = 'categories'


def desserts_view(request, category_id):
    queryset = Dessert.objects.filter(category_id=category_id)

    return render(
        request,
        'catalog/dessert_list.html',
        context={'desserts': queryset}
    )

