import config
import discord
from discord.ext import commands


def main():
    bot = commands.Bot(command_prefix = 'g!', intents = discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')

        for cog_file in config.COG_DIR.glob("*.py"):
            if cog_file != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

    
    @bot.command()
    async def ping(ctx):
        await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

    
    bot.run(config.TOKEN)


if __name__ == '__main__':
    main()