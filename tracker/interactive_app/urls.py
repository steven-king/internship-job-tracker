from django.conf.urls import patterns, url

from interactive_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name ='interactive_app_home')   
    )