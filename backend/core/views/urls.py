from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from graphene_django.views import GraphQLView

rest_doc = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

graphql_doc = [
    path("", GraphQLView.as_view(graphiql=True)),
]

urlpatterns = [
    path("rest/", include(rest_doc)),
    path("graph/", include(graphql_doc)),
    path("admin/", admin.site.urls),
]
