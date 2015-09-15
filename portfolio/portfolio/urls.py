from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.templatetags.static import static
from django.views.generic.base import RedirectView

from core.views import LandingView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', LandingView.as_view(), name='landing'),
    url(r'^resume|cv/$', RedirectView.as_view(url=static('docs/resume_Adam_Beagle.pdf'))),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
)
