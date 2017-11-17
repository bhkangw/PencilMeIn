from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^edit$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^(?P<id>\d+)$', views.edit),
    url(r'^logout$', views.logout),
]
