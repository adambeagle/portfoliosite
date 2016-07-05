from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^countdown-demo/$', TemplateView.as_view(template_name='projects/countdown.html'), name='countdown'),
    url(r'^swscroll-demo/$', TemplateView.as_view(template_name='projects/swscroll.html'), name='swscroll'),
    url(r'^swscroll-info/$', TemplateView.as_view(template_name='projects/swscroll-info.html'), name='swscroll-info'),
)
