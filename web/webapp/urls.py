from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/(?P<rfid_id>\w+)/$', 'beer.views.user_detail', name='user_detail'),
    url(r'^users/(?P<rfid_id>\w+)/edit$', 'beer.views.user_edit', name='user_edit'),
    url(r'^users/$', 'beer.views.user_list', name='user_list'),
    url(r'^search/$', 'beer.views.search', name='user_search'),
    url(r'^$', 'beer.views.front_page', name='front_page'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_graph/(?P<tap_number>\w+)/$', 'beer.views.get_graph'),
    url(r'^get_tap/(?P<tap_number>\w+)/$', 'beer.views.get_tap'),
    url(r'^get_last/(?P<tap_number>\w+)/$', 'beer.views.get_last'),
    url(r'^get_highest/(?P<tap_number>\w+)/$', 'beer.views.get_highest'),
    url(r'^get_fastest/(?P<tap_number>\w+)/$', 'beer.views.get_fastest'),
)

urlpatterns += staticfiles_urlpatterns()
