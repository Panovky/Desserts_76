from django.shortcuts import render
from gallery.models import Photo


def photos_view(request):

    return render(
        request,
        'catalog/category_list.html',
        context={'photos': Photo}
    )
