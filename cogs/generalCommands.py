import discord
from discord.ext import commands

helpResponses = {'default': 'Default Help Message',
                 'urban': 'Urban Help Message',
                 'urbanrandom': 'Urban Random Help Message',
                 'nextdef': 'NextDef Help Message',
                 '8ball': '8Ball Help Message'}

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xe8e805

    @commands.command(name='help')
    async def help(self, ctx, *arg):
        if len(arg) == 1 and helpResponses[arg[0].lower()]:
            embed = discord.Embed(color=self.color)
            embed.add_field(name=f'{arg[0].capitalize()} Help', value=helpResponses[arg[0].lower()])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=self.color)
            embed.add_field(name='Default Help', value=helpResponses['default'])
            await ctx.send(embed=embed)

