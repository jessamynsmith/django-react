from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'app/home.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)