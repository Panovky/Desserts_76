from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me_view, name='about_me'),
]
