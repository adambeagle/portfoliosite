from os.path import join, isfile

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.templatetags.static import static
from django.views.generic import DetailView, ListView

from .models import Article, Tag

class ArticleView(DetailView):
    template_name = 'blog/article.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        # Add banner_path to context, if banner image exists
        # Banner is assumed to be named 'banner.png' and live in a directory
        # inside /images/blog whose name is identical to the article's slug.
        slug = context['article'].slug
        banner_path = static('images/blog/{}/banner.png'.format(slug))
        
        if isfile(join(settings.BASE_DIR, banner_path[1:])):
            context['banner_path'] = str(banner_path)
            self.template_name = 'blog/article_with_banner.html'

        return context
    
class IndexView(ListView):
    model = Article
    paginate_by = 10
    template_name = 'blog/index.html'
    
class TagView(DetailView):
    model = Tag
    template_name = 'blog/tag.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_string'] = self.kwargs['slug']
        object = context['object']
        
        # If tag requested does not exist, object is None.
        # article_list is empty queryset in that case.
        if object is None:
            context['article_list'] = Article.objects.none()
        else:
            context['article_list'] = object.article_set.all()
        
        return context
        
    def get(self, request, *args, **kwargs):
        """
        In the case that the tag requested does not exist, rather than raise
        Http404, set self.object to None. get_context_data and the template 
        deal with this case appropriately.
        """
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
            
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
