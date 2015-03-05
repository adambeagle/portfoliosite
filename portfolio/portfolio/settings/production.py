from .base import *

STATIC_URL = 'http://adambeagle.com/static/'
STATIC_ROOT = BASE_DIR.parent.child('staticfiles')
ALLOWED_HOSTS = ['.adambeagle.com']
DEBUG = False
TEMPLATE_DEBUG = False
