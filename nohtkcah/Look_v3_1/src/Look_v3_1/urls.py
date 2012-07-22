from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('Look_v3_1',
    # Examples:
    # url(r'^$', 'Look_v3_1.views.home', name='home'),
    # url(r'^Look_v3_1/', include('Look_v3_1.foo.urls')),
    
    # upload a look photo
    url(r'^looks/upload/$', 'upload.views.upload'),
    # view a look
    url(r'^looks/(?P<look_id>\d+)/$', 'look.views.detail', name='look_detail'),
    # home
    url(r'^looks/$', 'look.views.index'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
    urlpatterns += staticfiles_urlpatterns()