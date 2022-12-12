from django.urls import path
from . import views

urlpatterns = [
    path('', views.photos_view, name='gallery'),
]
