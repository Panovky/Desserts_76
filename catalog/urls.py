from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^fillings/$', views.FillingsView.as_view(), name='fillings'),
    re_path(r'^fillings/learn-more/$', views.ContactsView.as_view(), name='learn-about-filling'),
    re_path(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
    re_path(r'^categories/(?P<category_id>\d+)/$', views.DessertsView.as_view(), name='desserts'),
    re_path(r'^categories/\d+/dessert-(?P<pk>\d+)/$', views.DessertDetailView.as_view(), name='some-dessert'),
    re_path(r'^categories/\d+/dessert-\d+/learn-more$', views.ContactsView.as_view(), name='learn-about-dessert'),
]