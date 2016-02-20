from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event/(?P<event_id>[0-9]+)/$', views.event, name='event'),
    # url(r'^event/$', views.events, name='events'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
    # url(r'^article/$', views.articles, name='articles'),
    url(r'^edit-article/', views.edit_article, name='edit-article'),
    url(r'^edit-event/', views.edit_event, name='edit-event'),
]