DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

TIME_ZONE = 'America/Los Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MIDDLEWARE_CLASSES = (
    'google.appengine.ext.ndb.django_middleware.NdbDjangoMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = ('templates')

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source')

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
)

MEDIA_URL = "/media/"

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
CACHE_BACKEND = "memcached://"

