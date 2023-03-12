from django.views.generic import TemplateView

class ReactView(TemplateView):
    template_name = "index.html" # a settings.py-ban megtalálja az útvonalat