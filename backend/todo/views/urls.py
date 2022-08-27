from django.urls import include, path

from .rest import urlpatterns as rest_patterns


urlpatterns = [
    path("rest/", include(rest_patterns)),
]
