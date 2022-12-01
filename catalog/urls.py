from django.urls import re_path
from django.urls import path

from . import views

urlpatterns = [
    re_path(r'^fillings/$', views.FillingsView.as_view(), name='fillings'),
    re_path(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
]