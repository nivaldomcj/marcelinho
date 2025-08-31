from loguru import logger
from .handlers.ping import PingHandler
import discord
from discord.ext import commands


class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.dm_messages = True
        super().__init__(command_prefix="!", intents=intents)

        # Initialize handlers
        self.ping_handler = PingHandler(self)

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

        # Handle messages through ping handler
        await self.ping_handler.handle_message(message)

        # TODO: handle DM messages
        if isinstance(message.channel, discord.DMChannel):
            logger.info(f"DM from {message.author}: {message.content}")

        # Process commands
        await self.process_commands(message)
