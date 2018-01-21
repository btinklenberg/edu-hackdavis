# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'content'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<subject_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^subject/$', views.subject, name='subject'),
    url(r'^create_subject/$', views.create_subject, name='create_subject'),
#    url(r'(?P<Blog_id>[0-9]+)/create_article/$', views.create_article, name='create_article'),
#    url(r'(?P<Blog_id>[0-9]+)/delete_article/$', views.delete_article, name='delete_article'),
#   url(r'(?P(Blog_id)[0-9]+)/delete_blog/$', views.delete_blog, name='delete_blog'),
]
