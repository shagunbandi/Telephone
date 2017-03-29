from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^search/(?P<number>[\w.@+-]+)/$', views.scrap, name='search'),
]

urlpatterns = format_suffix_patterns(urlpatterns)