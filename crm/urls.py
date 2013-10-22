from django.conf.urls import patterns, url

from crm import views

urlpatterns = patterns('',
    url(r'^(?P<student_id>\d+)/$', views.view_student, name='view_student'),
)
