"""
URL configuration for foobar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


@api_view(["GET"])
def _health_check(request):
    return HttpResponse("OK")


urlpatterns = [
    path("health/", _health_check),
    path("admin/", admin.site.urls),
    path("api/v1/", include(("api.urls", "api_v1"), namespace="v1")),
    path(
        "schema/",
        SpectacularAPIView.as_view(
            api_version="v1",
        ),
        name="schema",
    ),
    path("scheduler/", include("scheduler.urls")),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
