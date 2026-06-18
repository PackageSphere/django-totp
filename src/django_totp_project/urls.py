from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="docs", permanent=False)),
    path("admin/", admin.site.urls),
    path("api/auth/", include("django_totp.urls.jwt")),
    path("api/auth/", include("django_totp.urls.recovery")),
    path("api/auth/", include("django_totp.urls")),
    path("api/djoser/", include("djoser.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
]
