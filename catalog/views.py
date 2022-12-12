from django.shortcuts import render
from catalog.models import Filling, Category, Dessert


def fillings_view(request):

    return render(
        request,
        'catalog/filling_list.html',
        context={'fillings': Filling.objects.all()}
    )


def categories_view(request):

    return render(
        request,
        'catalog/category_list.html',
        context={'categories': Category.objects.all()}
    )


def desserts_view(request, category_id):
    desserts = Dessert.objects.filter(category_id=category_id)

    return render(
        request,
        'catalog/dessert_list.html',
        context={'desserts': desserts}
    )


def contacts_view(request):
    return render(
        request,
        'catalog/learn_more.html'
    )


def dessert_detail_view(request, dessert_id):
    dessert = Dessert.objects.filter(dessert_id=dessert_id).first()

    return render(
        request,
        'catalog/dessert_detail.html',
        context={'dessert': dessert}
    )
