from django.conf.urls import include, url

urlpatterns = [
    url(r'^activity/$', views.host0, name='hosting'),
    url(r'^activity/1$', views.host1, name='hosting'),
    url(r'^activity/2$', views.host2, name='hosting'),
    url(r'^activity/3$', views.host3, name='hosting'),
    url(r'^activity/4$', views.host4, name='hosting'),
    url(r'^activity/5$', views.host5, name='hosting'),
    url(r'^activity/6$', views.host6, name='hosting'),
    url(r'^activity/7$', views.host7, name='hosting'),
    url(r'^activity/8$', views.host7, name='hosting'),
]
