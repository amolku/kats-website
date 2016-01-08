""" Interviews URLS """

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^interview/(?P<pk>[0-9]+)/$', views.interview_detail, name='interview_detail'),
]
