from loguru import logger
import discord
from discord.ext import commands
from django.conf import settings
from django.core.management.base import BaseCommand


class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.dm_messages = True
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        """
        Called when bot is ready
        """
        logger.info(f"{self.user} has connected to Discord!")
        logger.info(f"Bot is in {len(self.guilds)} servers (guilds)")

        # List the guilds the bot is in
        for guild in self.guilds:
            logger.info(f"  - {guild.name} (ID: {guild.id})")

    async def on_message(self, message):
        """
        Handle incoming messages
        """
        if message.author == self.user:
            return

        # For now, just log DM messages
        if isinstance(message.channel, discord.DMChannel):
            logger.info(f"DM from {message.author}: {message.content}")

        # Process commands
        await self.process_commands(message)


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
