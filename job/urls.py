from django.conf.urls import url
from . import views
from django.db import models
from django.contrib.auth.models import User


app_name='job'

urlpatterns = [
    # /job/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /job/profile
    url(r'profile/$', views.ProfileView.as_view(), name='profile'),
    # /job/id/
    url(r'detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail' ),
    # /job/add/
    url(r'add/$', views.JobCreate.as_view(), name='job-add'),
    # /registration/create
    url(r'create/$', views.UserCreate.as_view(), name='user-create'),
    # /job/update/
    url(r'update/(?P<pk>[0-9]+)$', views.JobUpdate.as_view(), name='job-update'),
    # /job/delete/
    url(r'delete/(?P<pk>[0-9]+)$', views.JobDelete.as_view(), name='job-delete'),
]
