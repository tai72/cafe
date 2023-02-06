from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class MenuView(generic.TemplateView):
    template_name = "menu.html"
