from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.templatetags.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from core.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', RedirectView.as_view(url='/blog')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^resume/$', RedirectView.as_view(url=static('docs/resume_Adam_Beagle.pdf'))),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
)
