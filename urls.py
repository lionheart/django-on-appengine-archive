from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'views.index'),
    url(r'^sign$', 'views.sign'),
)

