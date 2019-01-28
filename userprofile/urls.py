#user profile app

from django.conf.urls import url
from . import views


urlpatterns = [
     url(r'^$', views.myFun, name = 'myFun'),
     url(r'^(?P<user_id>[0-9]+)/$', views.userDetails, name = 'userDetails')
]

