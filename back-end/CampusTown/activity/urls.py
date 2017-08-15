from django.conf.urls import include, url
from django.contrib import admin
from activity.views import host2,host1,host5,host4
from . import views

urlpatterns = [
   # url(r'^activity/$', views.host0, name='hosting'),
   url(r'^activity/1/$',views.host1,name='host1'),
   url(r'^activity/2$', views.host2, name='hosting language'),
   #url(r'^activity/2/$', views.host2_category, name='hosting category'),
   # url(r'^activity/3$', views.host3, name='hosting'),
   url(r'^activity/4$', views.host4, name='host4'),
   url(r'^activity/5$', views.host5, name='host5'),
   # url(r'^activity/6$', views.host6, name='hosting'),
   # url(r'^activity/7$', views.host7, name='hosting'),
   # url(r'^activity/8$', views.host8, name='hosting'),
]
