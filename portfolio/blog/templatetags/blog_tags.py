from django import template

register = template.Library()

@register.inclusion_tag('tags/breadcrumb.html')
def breadcrumb(title, *steps):
    return {'title' : title, 'steps' : steps}