"""
django_totp.signals
===================

Public signal definitions for django-totp.
"""

from django.dispatch import Signal


# User successfully completes TOTP enrollment.
totp_created = Signal()

# User disables TOTP authentication.
totp_disabled = Signal()

# User generates a new set of backup codes.
backup_codes_rotated = Signal()

# User successfully completes 2FA authentication
# using either a TOTP code or a backup code.
totp_login_succeeded = Signal()

# User successfully authenticates without requiring TOTP.
non_totp_login_succeeded = Signal()

# user recovers their account after losing access to their TOTP device.
totp_recovery_succeeded = Signal()
