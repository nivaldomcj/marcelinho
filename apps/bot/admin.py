from django.contrib import admin

from .models import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'discord_guild_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'discord_guild_id')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('discord_guild_id', 'name', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
        }),
    )
