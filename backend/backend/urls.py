from django.urls import include, path

from core.views.urls import urlpatterns as core
from person.views.urls import urlpatterns as person
from todo.views.urls import urlpatterns as todo

urlpatterns = [
    path("", include(core)),
    path("", include(person)),
    path("", include(todo)),
]
