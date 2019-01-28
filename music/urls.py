#music apps
from django.conf.urls import url
from . import views

urlpatterns = [
    #music url
    url(r'^$', views.index, name='index'),
    
    #music/id (eg: 712)/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name ='details'),
]
