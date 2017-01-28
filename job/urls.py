from django.conf.urls import url
from . import views

app_name='job'

urlpatterns = [
    # /job/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /job/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail' ),
    # /job/add/
    url(r'job/add/$', views.JobCreate.as_view(), name='job-add'),
]