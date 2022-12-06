from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewsView.as_view(), name='reviews'),
    re_path(r'^new/$', views.create_new_review, name='new-review')
]
