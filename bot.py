import asyncio
import discord
import json
import os
from cogs import *
from discord.ext import commands
from dotenv import load_dotenv

f = open('config.json')
config = json.load(f)
f.close()

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config['command_symbol'], intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    """Sends a message in the terminal with the name
    of the bot, after the bot has logged on
    """

    print(f'Logged on as {bot.user}')
    await load_cogs()

async def load_cogs():
    """Loads all the cogs for the discord bot
    """
    await bot.add_cog(Urban(bot))
    await bot.add_cog(Nasa(bot))
    await bot.add_cog(Text(bot))
    await bot.add_cog(Eight(bot, config['cogs']['8ball']))
    await bot.add_cog(Help(bot))

def main():
    bot.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()

