import logging
import os
import sys

from google.appengine.dist import use_library

for k in [k for k in sys.modules if k.startswith('django')]:
    del sys.modules[k]

# You can change this if you'd like.
use_library('django', '1.2')

# Must set this env var before importing any part of Django
# 'project' is the name of the project created with django-admin.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Google App Engine imports.
from google.appengine.ext.webapp import util

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch

# Force Django to reload its settings.
from django.conf import settings

from google.appengine.api import memcache
sys.modules['memcache'] = memcache

settings._target = None

def log_exception(*args, **kwds):
    logging.exception('Exception in request:')

signal = django.dispatch.Signal()

# Log errors.
signal.connect(log_exception, django.core.signals.got_request_exception)

# Unregister the rollback event handler.
signal.disconnect(django.db._rollback_on_exception, django.core.signals.got_request_exception)

def main():
    # Create a Django application for WSGI.
    application = django.core.handlers.wsgi.WSGIHandler()

    # Run the WSGI CGI handler with that application.
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()


