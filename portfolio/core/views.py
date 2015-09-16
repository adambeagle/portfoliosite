from django.templatetags.static import static
from django.views.generic import ListView

from projects.models import Project

class LandingView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'landing.html'
    