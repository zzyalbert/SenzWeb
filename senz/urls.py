from django.conf.urls import patterns, include, url

urlpatterns = patterns('senz.views',
    url(r'^$', 'index'),
    url(r'^get_poi/$', 'get_poi'),
    
)
