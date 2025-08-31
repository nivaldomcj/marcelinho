from loguru import logger
from django.conf import settings
from django.core.management.base import BaseCommand
from utils.discord import DiscordBot


class Command(BaseCommand):
    help = "Run the Discord bot"

    def handle(self, *args, **options):
        if (
            not hasattr(settings, "DISCORD_BOT_TOKEN")
            or not settings.DISCORD_BOT_TOKEN
        ):
            logger.error(
                "DISCORD_BOT_TOKEN not found in settings or .env file"
            )
            return

        logger.success("Starting Discord bot...")

        bot = DiscordBot()

        try:
            bot.run(settings.DISCORD_BOT_TOKEN)
        except KeyboardInterrupt:
            logger.success("Bot stopped by user")
        except Exception as e:
            logger.error(f"Bot crashed: {e}")
