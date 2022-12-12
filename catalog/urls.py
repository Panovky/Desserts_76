from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^fillings/$', views.fillings_view, name='fillings'),
    re_path(r'^fillings/learn-more/$', views.contacts_view, name='learn-about-filling'),
    re_path(r'^categories/$', views.categories_view, name='categories'),
    re_path(r'^categories/(?P<category_id>\d+)/$', views.desserts_view, name='desserts'),
    re_path(r'^categories/\d+/dessert-(?P<dessert_id>\d+)/$', views.dessert_detail_view, name='some-dessert'),
    re_path(r'^categories/\d+/dessert-\d+/learn-more$', views.contacts_view, name='learn-about-dessert'),
]