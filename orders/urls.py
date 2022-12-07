from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_new_order, name='new-order'),
    re_path(r'^success/$', views.show_success, name='success'),
]

