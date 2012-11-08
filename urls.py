from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'guestbook.views.index'),
    url(r'^sign$', 'guestbook.views.sign'),
)

