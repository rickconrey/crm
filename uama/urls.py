from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uama.views.home', name='home'),
    # url(r'^uama/', include('uama.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^crm/', include('crm.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'template_name':'crm/login.html',}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page':'/login/',}),
    url(r'^admin/', include(admin.site.urls)),
)
