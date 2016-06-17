from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process ),
    url(r'^courses/destroy/(?P<id>\d+)$', views.toremove ),
    url(r'^returnn$', views.returnn ),
    url(r'^remove$', views.remove ),
]
