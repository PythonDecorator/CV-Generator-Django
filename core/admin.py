"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ["id"]
    list_display = ["email", "first_name", "last_name", "is_staff"]
    fieldsets = (
        (None, {"fields": ("password", "first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active",
                                       "is_staff",
                                       "is_superuser")}),
        (_("Important dates"), {"fields": ("date_joined", "last_login",)}),
    )
    readonly_fields = ["date_joined", "last_login"]

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "first_name",
                "last_name",
                "is_active",
                "is_staff",
                "is_superuser",
            ),
        }),
    )


admin.site.site_header = "CV App"
admin.site.site_title = "CV Gen"
admin.site.index_title = "CV Gen"

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile)
