from .base import *

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.parent.child('staticfiles')
ALLOWED_HOSTS = ['.adambeagle.com']
DEBUG = False
TEMPLATE_DEBUG = False
