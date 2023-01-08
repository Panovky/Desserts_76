from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotosView.as_view(), name='gallery'),
]
