from os.path import basename
import re

from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

# ============================================================================
# BASE CLASSES
class BaseStaticFile(models.Model):
    """
    Designed for use with models that represent or point to a static asset.
    Provides static_path and filename cached properties.
    """
    def __str__(self):
        return self.static_path
    
    @cached_property
    def filename(self):
        return basename(self.full_path)
    
    @cached_property
    def static_path(self):
        return re.match(
            r".*/static/(.+)$", self.full_path
        ).group(1)
        
    class Meta:
        abstract = True

class BaseImage(BaseStaticFile):
    """
    Abstract base for an object representing an optionally captioned image.
    """
    # Cast to str for 'path' argument is necessary.
    # Migrations will fail in dealing with Path object otherwise
    full_path = models.FilePathField(
        path=str(settings.BASE_DIR.child('static', 'images')), 
        recursive=True,
        max_length=128,
    )
    alt_text = models.CharField(max_length=64, null=True, blank=True)
    caption  = models.CharField(max_length=256, null=True, blank=True)
        
    @cached_property
    def thumbnail_path(self):
        return re.sub(
            r"^images/(?:.*/)*(.+)$", 
            r'images/tn/\1',
            self.static_path
        )

    class Meta:
        abstract = True

class BaseLink(models.Model):
    """
    Abstract base for an object representing a hyperlink.
    """
    url = models.URLField()
    text = models.CharField(max_length=64)
    title = models.CharField(max_length=32)
    
    def __str__(self):
        return "{0} ({1})".format(self.text, self.url)
        
    class Meta:
        abstract = True
        ordering = ['text']

#=============================================================================
class Image(BaseImage):
    """Use with ForeignKey to give external model single image."""
    pass

class Link(BaseLink):
    pass