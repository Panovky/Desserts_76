from django.shortcuts import render
from gallery.models import Photo


def photos_view(request):

    return render(
        request,
        'gallery/photo_list.html',
        context={'photos': Photo.objects.all()}
    )
