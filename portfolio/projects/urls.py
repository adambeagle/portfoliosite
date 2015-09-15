from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^play-countdown/$', TemplateView.as_view(template_name='projects/countdown.html'), name='countdown'),
)
