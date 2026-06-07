"""
django_totp.urls
================

URL patterns for TOTP authentication.
"""

from rest_framework.routers import DefaultRouter

from ..views import TotpViewSet

router = DefaultRouter()
router.register(r"totp", TotpViewSet, basename="totp")

urlpatterns = router.urls
