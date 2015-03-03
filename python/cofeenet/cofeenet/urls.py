from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cofeenet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^celular/', include('celular.urls', namespace = 'celular')),
    url(r'^protector/', include('protector.urls', namespace = 'protector')),
    url(r'^admin/', include(admin.site.urls)),
)
