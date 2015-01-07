from django.conf.urls import patterns, url

from contact import views

urlpatterns = patterns('',
    url(r'^$', views.my_view, name='index'),
)