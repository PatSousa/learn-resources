from django.conf.urls import url

from .views import ResourceList, ResourceDetail

urlpatterns = [
    url(r'^resources/$', ResourceList.as_view(), name='list'),
    url(r'^resources/(?P<pk>[0-9]+)/$', ResourceDetail.as_view(), name='detail'),
]