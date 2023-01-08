from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from catalog.models import Filling, Category, Dessert


class FillingsView(generic.ListView):
    model = Filling
    context_object_name = 'fillings'


class CategoriesView(generic.ListView):
    model = Category
    context_object_name = 'categories'


class DessertsView(generic.ListView):
    model = Dessert

    def get_context_data(self, **kwargs):
        context = super(DessertsView, self).get_context_data(**kwargs)
        context['desserts'] = Dessert.objects.filter(category_id=self.kwargs.get('category_id'))
        return context


class ContactsView(TemplateView):
    template_name = 'catalog/learn_more.html'


class DessertDetailView(DetailView):
    model = Dessert

    def get_context_data(self, **kwargs):
        context = super(DessertDetailView, self).get_context_data(**kwargs)
        context['dessert'] = Dessert.objects.filter(dessert_id=self.kwargs.get('pk')).first()
        return context
