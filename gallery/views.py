from django.views import generic
from gallery.models import Photo

class PhotosView(generic.ListView):
    model = Photo
    context_object_name = 'photos'