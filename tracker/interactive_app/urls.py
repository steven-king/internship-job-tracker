from django.conf.urls import patterns, include, url

from interactive_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name ='interactive_app_home'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^user/$', views.userList, name='interactive_app_user_list'),
    url(r'^user/(?P<pk>\d+)$', views.user, name='interactive_app_user'),
	url(r'^organization/$', views.organizationList, name='interactive_app_organization_list'),
	url(r'^city/$', views.cityList, name='interactive_app_city_list'),
	url(r'^city/(?P<pk>\d+)$', views.city, name='interactive_app_city')
    )