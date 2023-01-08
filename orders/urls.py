from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MakeNewOrder.as_view(), name='new-order'),
    re_path(r'^success/$', views.ShowSuccess.as_view(), name='success'),
]

