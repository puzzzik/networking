from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from drf_spectacular.authentication import OpenApiAuthenticationExtension
from backend.authentication.backends import JWTAuthentication


class JWTAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = JWTAuthentication  # full import path OR class ref
    name = 'JWTAuthentication'  # name used in the schema

    def get_security_definition(self, auto_schema):
        return {
            'type': 'session',
            'name': 'session',
        }


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
