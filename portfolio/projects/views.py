from django.templatetags.static import static
from django.views.generic import ListView

from .models import Project

class ProjectIndexView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/project_index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_path'] = static('images/projects/banner.png')
        
        return context