from django.db import models

from apps.core.models import BaseModel


class Server(BaseModel):
    discord_guild_id = models.CharField(
        max_length=20,
        unique=True,
        help_text="Discord Guild ID (Server ID)"
    )
    name = models.CharField(
        max_length=255,
        help_text="Discord server name"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Should daily bot be active in this server?"
    )

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'

    def __str__(self):
        return f"{self.name} ({self.discord_guild_id})"
