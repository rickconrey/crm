from django.conf.urls import patterns, url
from crm.views import StudentUpdate, ContactUpdate

from crm import views

urlpatterns = patterns('',
    url(r'^(?P<student_id>\d+)/$', views.listing, name='listing'),
    url(r'^update/(?P<pk>\d+)/$', StudentUpdate.as_view(),
        name='student_update'),
    url(r'^contactup/(?P<pk>\d+)/$', ContactUpdate.as_view(),
        name='contact_update'),
    #url(r'^(?P<student_id>\d+)/$', views.view_student, name='view_student'),
)
