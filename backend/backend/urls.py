from django.urls import include, path

from person.views.urls import urlpatterns as person
from todo.views.urls import urlpatterns as todo
from core.views.urls import urlpatterns as core


urlpatterns = [
    path("", include(core)),
    path("", include(person)),
    path("", include(todo)),
]
