from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^activity/$', views.host, name='hosting'),
    url(r'^activity/0/$', views.host0, name='host0'),
    url(r'^activity/1/$', views.host1, name='host1'),
    url(r'^activity/2/$', views.host2, name='host2'),
    url(r'^activity/3/$', views.host3, name='host3'),
	url(r'^activity/4/(?P<pk>\d+)/$', views.host4, name='host4'),
    url(r'^activity/5/(?P<pk>\d+)/$', views.host5, name='host5'),
    url(r'^activity/6/(?P<pk>\d+)/$', views.host6, name='host6'),
    url(r'^activity/7/(?P<pk>\d+)/$', views.host7, name='host7'),
    url(r'^activity/8/(?P<pk>\d+)/$', views.host7, name='host8'),
]
