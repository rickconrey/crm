from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from crm.views import StudentUpdate, ContactUpdate, RelationshipUpdate
from crm.views import Search, Scanner
from crm import views

urlpatterns = patterns('',
    url(r'^(?P<student_id>\d+)/$', views.listing, name='listing'),
    url(r'^update/(?P<pk>\d+)/$', login_required(StudentUpdate.as_view(),
        login_url='/login/'),
        name='student_update'),
    url(r'^contactup/(?P<pk>\d+)/$', login_required(ContactUpdate.as_view(),
        login_url='/login/'),
        name='contact_update'),
    url(r'^relup/(?P<pk>\d+)/$', login_required(RelationshipUpdate.as_view(),
        login_url='/login/'),
        name='relationship_update'),
    url(r'^search/$', login_required(Search.as_view(),login_url='/login/'),
        name='search_view'),
    url(r'^scanner/$', Scanner.as_view(), name='scanner'),
)
