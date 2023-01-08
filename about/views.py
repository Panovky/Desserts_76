from django.views.generic.base import TemplateView


class AboutMeView(TemplateView):
    template_name = 'about/about_me.html'
