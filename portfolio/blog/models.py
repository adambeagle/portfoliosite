import re

from bs4 import BeautifulSoup
from django.db import models
from django.db.models.signals import m2m_changed, pre_delete
from django.templatetags.static import static
from django.utils.text import slugify
from markdown import markdown
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

PYGMENT_CSS_CLASS = 'pygment'

def auto_heading_ids(soup):
    """
    Return soup with automatic slugified ids to any headings ("h#" tags).
    Expects bs4.BeautifulSoup object
    """
    for h in soup.find_all(re.compile('h\d$')):
        s = ''.join(h.strings)
        h['id'] = slugify(s)
        
    return soup

def make_table_of_contents(soup, min_headings=5, label_headings=True):
    """
    Return new BeautifulSoup object containing table of contents for 
    content in 'soup.' Any headings present are included, and are 
    expected to have ids.
    
    If total number of headings is fewer than min_headings, an empty string
    is returned.
    
    Expects bs4.BeautifulSoup object.
    """
    toc = BeautifulSoup()
    
    count_stack = []
    current_ol = None
    previous_li = toc
    previous_heading_name = 'h0'
    i = 0
    
    for i, h in enumerate(soup.find_all(re.compile('h\d$'))):
        if h.name > previous_heading_name:
            current_ol = toc.new_tag('ol')
            count_stack.append(0)
            previous_li.append(current_ol)
        
        else: 
            # Step back to correct ol
            skip = int(previous_heading_name[1]) - int(h.name[1])
            for j in range(skip):
                count_stack.pop()
                current_ol = current_ol.parent.parent
            
        count_stack[-1] += 1
        new_li = soup.new_tag('li')
        a = toc.new_tag('a', href='#' + h['id'])
        a.string = ''.join(h.strings)
        
        if label_headings:
            label_span = soup.new_tag('span')
            label_span['class'] = 'heading-number'
            label_span.string = '.'.join(map(str, count_stack))
            print(h)
            h.insert(0, " ")
            print(h)
            h.insert(0, label_span)
            print(h, '\n')
        
        new_li.append(a)
        current_ol.append(new_li)
        previous_li = new_li
        previous_heading_name = h.name

    return toc if i >= min_headings - 1 else ''

def pygmentize(soup):
    """
    Return 'soup' with code blocks pygmentized.
    
    Expects bs4.BeautifulSoup object
    """
    for code in soup.select('pre > code'):
        
        new_soup = BeautifulSoup(
            highlight(
                code.string, 
                PythonLexer(), 
                HtmlFormatter(cssclass=PYGMENT_CSS_CLASS)
            )
        )
        code.clear()
        for element in new_soup:
            code.append(element)
            
    return soup

def staticify_img_srcs(soup):
    """
    Return `soup` with img tag's src attributes fixed to be static paths,
    as though the src attribute was the argument to a {% static %} template
    tag.
    
    Expects bs4.BeautifulSoup object.
    """
    for img in soup.find_all('img'):
        img['src'] = static(img.get('src'))
        
    return soup



class Tag(models.Model):
    slug = models.SlugField(max_length=32)
    count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.slug
        
    def save(self, *args, **kwargs):
        #self.count = len(self.article_set.all())
        
        return super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['-count']

class Article(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=128, default='', null=True, blank=True)
    slug = models.SlugField(max_length=32, default='')
    posted = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    
    # Auto-created on save
    content_html  = models.TextField()
    toc = models.TextField()
    last_edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_title

    def save(self, *args, **kwargs):
        soup = BeautifulSoup(markdown(self.content, 
            extensions=['markdown.extensions.footnotes']
        ))
        soup = auto_heading_ids(soup)
        soup = staticify_img_srcs(soup)
        soup = pygmentize(soup)
        toc = make_table_of_contents(soup, label_headings=True)
        
        self.toc = str(toc)
        self.content_html = str(soup)
        
        return super().save(*args, **kwargs)
        
    @property
    def full_title(self):
        if self.subtitle:
            return '{} - {}'.format(self.title, self.subtitle)
        else:
            return self.title
        
    class Meta:
        ordering = ['-posted']

def article_changed(sender, **kwargs):
    """Update Tag.count attributes when articles added, updated, or deleted."""
    article = kwargs['instance']

    # Delete or tag removal
    # Note in case of update with no change for a tag, it "balances out" because
    # it is cleared then added.
    if sender is Article or kwargs['action'] == 'pre_clear':
        for tag in article.tags.all():
            tag.count = max(0, tag.count - 1)
            tag.save()
            
    # Add or update
    elif kwargs['action'] == 'post_add':
        for tag in article.tags.all():
            tag.count += 1
            tag.save()

m2m_changed.connect(article_changed, sender=Article.tags.through)
pre_delete.connect(article_changed, sender=Article)
