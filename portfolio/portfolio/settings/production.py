from .base import *

STATIC_URL = 'http://adambeagle.com/static/'
STATIC_ROOT = BASE_DIR.parent.child('staticfiles')
ALLOWED_HOSTS = ['*']
DEBUG = False
TEMPLATE_DEBUG = False
