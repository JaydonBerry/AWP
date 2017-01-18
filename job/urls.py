from django.conf.urls import url
from . import views

urlpatterns = [
    # /job/
    url(r'^$', views.index, name='index'),
    # /job/id/
    url(r'^(?P<job_id>[0-9]+)/$', views.detail, name='detail' ),
]