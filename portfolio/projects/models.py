from django.db import models

from core.models import Image, Link

class Project(models.Model):
    title = models.CharField(max_length=32, primary_key=True)
    slug = models.SlugField()
    image = models.ForeignKey(Image)
    
    type = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    technology = models.CharField(max_length=64)
    
    description = models.TextField()
    
    source_url = models.OneToOneField(
        Link, 
        related_name="source_project", 
        null=True, 
        blank=True
    )
    
    live_url = models.OneToOneField(
        Link, 
        related_name="liveurl_project", 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-slug']