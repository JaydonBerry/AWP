from django.conf.urls import url
from . import views

app_name='job'

urlpatterns = [
    # /job/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /job/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /job/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail' ),
    # /job/add/
    url(r'add/$', views.JobCreate.as_view(), name='job-add'),
    # /job/update/
    url(r'update/(?P<pk>[0-9]+)/$', views.JobUpdate.as_view(), name='job-update'),
    # /job/delete/
    url(r'job/(?P<pk>[0-9]+)/delete/$', views.JobDelete.as_view(), name='job-delete'),
]