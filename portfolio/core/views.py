from django.templatetags.static import static
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_path'] = static('images/banners/tahq_banner.png')
        
        return context