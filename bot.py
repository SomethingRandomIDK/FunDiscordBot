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
helpList = {'commands': {},
        'features': {}}

@bot.event
async def on_ready():
    """Sends a message in the terminal with the name of the bot, after the bot
    has logged on it loads all the cogs
    """

    print(f'Logged on as {bot.user}')
    await load_cogs()

    loadHelp()

async def load_cogs():
    """Loads all the cogs for the discord bot
    """
    allCogs = {'urban': Urban(bot, config['cogs']['urban']),
               'nasa': Nasa(bot, config['cogs']['nasa'], os.getenv('NASA_API')),
               '8ball': Eight(bot, config['cogs']['8ball']),
               'message': Text(bot, config['cogs']['message'])}

    for x in config['cogs']:
        if config['cogs'][x]['active']:
            await bot.add_cog(allCogs[x])

def loadHelp():
    '''Loads all the help dictionaries from all available cogs for the help
    command
    '''
    for x in bot.cogs:
        if 'commands' in bot.cogs[x].help:
            helpList['commands'].update(bot.cogs[x].help['commands'])
        if 'features' in bot.cogs[x].help:
            helpList['features'].update(bot.cogs[x].help['features'])

@bot.command(name='help')
async def help(ctx, *arg):
    '''Gives a list of all possible commands as well as lets you search a
    command to get a description about what it does and how to use it
    '''
    embed = discord.Embed(title='Bot Help', color=int(config['help']['color'], 16))
    if len(arg) > 0 and arg[0].lower() in helpList['commands']:
        comm = helpList['commands'][arg[0].lower()]
        csUsage = '`' + config['command_symbol'] + comm['usage'][1:]
        embed.add_field(name='Command Usage', value=csUsage, inline=False)
        embed.add_field(name='Command Description', value=comm['description'], inline=False)
    else:
        commList = ''
        for x in helpList['commands']:
            commList += x
            commList += '\n'
        commList += '\nYou can use `?help [command]` for more information about each of these commands'

        embed.add_field(name='Command List', value=commList)

    await ctx.send(embed=embed)

def main():
    bot.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()

