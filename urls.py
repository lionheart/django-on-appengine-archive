from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='home'),
)

