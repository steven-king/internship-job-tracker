from django.conf.urls import patterns, include, url

from interactive_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name ='interactive_app_home'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^user/$', views.user, name='interactive_app_user'),
	url(r'^organization/$', views.organization, name='interactive_app_organization'),
	url(r'^city/$', views.city, name='interactive_app_city')
    )