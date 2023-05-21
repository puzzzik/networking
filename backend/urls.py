"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import app.urls
import authentication.urls
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from authentication.backends import JWTAuthentication
router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet, basename='products')
# router.register(r'order', OrderViewSet)
# router.register(r'cart', CartViewSet)
schema_view = get_schema_view(
    openapi.Info(
      title="Service API",
      default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    # authentication_classes=[JWTAuthentication]
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('', include(spectacular.urls)),
    # path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', include(authentication.urls, namespace='authentication')),
    path('', include(app.urls))
]
