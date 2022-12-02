from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^fillings/$', views.FillingsView.as_view(), name='fillings'),
    re_path(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
    re_path(r'^categories/(?P<category_id>\d+)/$', views.desserts_view, name='desserts'),
]