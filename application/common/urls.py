from django.conf.urls import patterns, url

urlpatterns = patterns('common.views',
    url(r'^_ah/warmup', 'warmup', name='warmup'),
    url(r'^$', 'home', name='home'),
)