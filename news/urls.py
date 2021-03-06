from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event/(?P<event_id>[0-9]+)/$', views.event, name='event'),
    url(r'^events/$', views.events, name='events'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^article/(?P<article_id>[0-9]+)/edit', views.edit_article, name='edit-article'),
    url(r'^event/(?P<event_id>[0-9]+)/edit', views.edit_event, name='edit-event'),
    url(r'^upload-file/', views.upload_file, name='upload-file'),
    url(r'^upload-done/', views.upload_done, name='upload-done'),
]
