from django.conf.urls import patterns, url

from .views import ProjectIndexView

urlpatterns = patterns('',
    url(r'^', ProjectIndexView.as_view(), name="index"),
)
