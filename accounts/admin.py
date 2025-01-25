from django.contrib import admin
from .models import User , Profile
from django.contrib.auth.admin import UserAdmin


class CustumeUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "is_staff")
    ordering = ("email",)


admin.site.register(User , CustumeUserAdmin)
admin.site.register(Profile)


