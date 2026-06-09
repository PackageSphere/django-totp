"""
django-totp.admin
=================

Admin configuration for django-totp models.
"""

from django.contrib import admin
from django.db.models import Count, Q

from .models import BackupCode, Totp


class BackupCodeInline(admin.TabularInline):
    model = BackupCode
    extra = 0
    can_delete = False

    fields = ("masked_code", "is_used", "created_at")
    readonly_fields = ("masked_code", "is_used", "created_at")

    show_change_link = False

    @admin.display(description="Code")
    def masked_code(self, obj):
        return f"{obj.code[:4]}***********"


@admin.register(Totp)
class TotpAdmin(admin.ModelAdmin):
    list_display = (
        "user_email",
        "username",
        "backup_code_available",
        "created_at",
    )

    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "user__username",
    )

    list_filter = ("created_at",)

    readonly_fields = (
        "user",
        "masked_secret_key",
        "created_at",
    )

    fields = (
        "user",
        "masked_secret_key",
        "created_at",
    )

    list_select_related = ("user",)

    list_per_page = 20

    date_hierarchy = "created_at"

    ordering = ("-created_at",)

    inlines = [BackupCodeInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        return queryset.annotate(
            available_backup_codes=Count(
                "backup_codes",
                filter=Q(backup_codes__is_used=False),
            ),
            total_backup_codes=Count("backup_codes"),
        )

    @admin.display(description="User Email", ordering="user__email")
    def user_email(self, obj):
        return obj.user.email

    @admin.display(description="Username", ordering="user__username")
    def username(self, obj):
        return obj.user.username

    @admin.display(
        description="Backup Codes",
        ordering="available_backup_codes",
    )
    def backup_code_available(self, obj):
        return f"{obj.available_backup_codes}/{obj.total_backup_codes}"

    @admin.display(description="Secret Key")
    def masked_secret_key(self, obj):
        return f"{obj.secret_key[:4]}***********"
