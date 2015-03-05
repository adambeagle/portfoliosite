from django.contrib import admin

from .models import Article, Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' :  ('title', )}
    fields = ('title', 'subtitle', 'slug',  'posted',  'tags', 'content')
    
class TagAdmin(admin.ModelAdmin):
    fields = ['slug', 'count']
    readonly_fields = ['count']
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
