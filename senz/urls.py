from django.conf.urls import patterns, include, url

urlpatterns = patterns('senz.views',
    url(r'^$', 'index'),
    url(r'^get_poi/$', 'get_poi'),
    url(r'^get_senz/$', 'get_senz'),
    url(r'^motion/$', 'motion'),
    url(r'^static_info/$', 'static_info'),
    
)
