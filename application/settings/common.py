try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

import os
import sys
from django.contrib.messages import constants as messages

DEPLOYMENT_NAME = os.environ.get('USER', 'unspecified')

SITE_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), '../')

# include ext for external deps
sys.path.append(os.path.join(SITE_ROOT, 'ext'))

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'compressor.finders.CompressorFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.tz",
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

#AUTH_PROFILE_MODULE = ''

ROOT_URLCONF = 'urls'

LOGIN_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

INTERNAL_IPS = ['127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'common',
    #'south'
]
if has_djangoappengine:
    INSTALLED_APPS = ('djangoappengine',) + INSTALLED_APPS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DEBUG = True
SECRET_KEY = 'probablyshoulduseyourownuniquekeyhere'

if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or
        os.getenv('SETTINGS_MODE') == 'prod'):
    DEBUG = False

    DEPLOYMENT_NAME = 'production'
    DEPLOYMENT_VERSION = os.environ.get('CURRENT_VERSION_ID', 'developer')

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'TIMEOUT': 0,
        }
    }

    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': '', # GAE mySQL instance
            'NAME': '' # GAE mySQL name
        },
    }

    SECRET_KEY = 'probablyshoulduseanotheruniquekeyhere'

    MINIMUM_CLIENT_VERSIONS = {
        'Nalu': [3, 0, 15],
        'android': None,
        'web': None,
    }

else:
    from settings.local import *
