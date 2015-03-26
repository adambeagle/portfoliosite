from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import ProjectIndexView

urlpatterns = patterns('',
    url(r'^$', ProjectIndexView.as_view(), name="index"),
    url(r'^play-countdown/$', TemplateView.as_view(template_name='projects/countdown.html'), name='countdown'),
)
