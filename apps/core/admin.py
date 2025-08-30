from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-created_at',)

    readonly_fields = UserAdmin.readonly_fields + \
        ('id', 'created_at', 'updated_at')

    fieldsets = UserAdmin.fieldsets + (
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
