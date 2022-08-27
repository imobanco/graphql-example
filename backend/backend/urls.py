from django.contrib import admin
from django.urls import include, path

from person.views.urls import urlpatterns as person

apis_patterns = [
    path("", include(person)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns.extend(apis_patterns)
