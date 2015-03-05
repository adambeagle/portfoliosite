from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import ArticleView, IndexView, TagView#, tags_view

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleView.as_view(), name='article'),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagView.as_view(), name='tag'),
    #url(r'^tag/(?P<tags>[\w-]+(?:\+[\w-]+))/$', tags_view,  name='tags')
)
