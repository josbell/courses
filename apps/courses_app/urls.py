from django.conf.urls import url
from . import views

##Need to modify regex on display Remove Page to allow for url parameter to be passed

urlpatterns = [
    url(r'^$', views.index),
    url(r'^displayRemovePage/(?P<id>\d+)$', views.displayRemovePage),
    url(r'^add$', views.add),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]
