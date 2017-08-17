from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^activity/(?P<pk>\d+)/$', views.detail, name='detail'),
]
