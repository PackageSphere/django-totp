"""
django_totp.throttle
====================

Throttle configuration for the TOTP API endpoints.
"""

from django.conf import settings as django_settings
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from warnings import deprecated

THROTTLE_RATE = getattr(django_settings, "TOTP_THROTTLE_RATE", "10/minute")


class TotpUserThrottle(UserRateThrottle):
    """Apply a configurable rate limit to authenticated TOTP-related API actions."""

    def get_rate(self):
        return THROTTLE_RATE


@deprecated(
    "Use TotpUserThrottle instead of TotpThrottle. This will be removed in a future version."
)
class TotpThrottle(TotpUserThrottle):
    """Deprecated alias for TotpUserThrottle."""


class TotpAnonThrottle(AnonRateThrottle):
    """Apply a configurable rate limit to anonymous TOTP-related API actions."""

    def get_rate(self):
        return THROTTLE_RATE
