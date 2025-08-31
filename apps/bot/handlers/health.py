import discord


class HealthHandler:
    def __init__(self, bot):
        self.bot = bot

    async def handle_message(self, message):
        if message.author == self.bot.user:
            return

        # This is just valid for text messages, not DMs
        if not isinstance(message.channel, discord.TextChannel):
            return

        # Just to check if bot is alive or not
        if self.bot.user.mentioned_in(message):
            await message.channel.send(f"{message.author.mention}, me chamou?")
        elif "marcelinho" in message.content.lower():
            await message.channel.send("👀")
