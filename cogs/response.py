import discord
from config import session
from UnlimitedGPT import ChatGPT
from discord.ext import commands


class Response(commands.Cog):
    def __init__(self, bot, session_token: str = '') -> None:
        self.bot = bot
        self.TOKEN = session_token

        self.api = ChatGPT(session,
                           chrome_args = None,
                           disable_moderation = True)
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        if "gato" in message.content.lower():
            content = message.content

            async with message.channel.typing():
                try:
                    response = self.api.send_message(content, input_mode = "INSTANT")
                    await message.channel.send(response)

                except Exception as e:
                    print(e)
                    await message.channel.send(f"Error: {e}")


async def setup(bot):
    await bot.add_cog(Response(bot, session))