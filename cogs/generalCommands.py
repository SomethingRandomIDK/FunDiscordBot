import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xe8e805

        defaultEmbed = discord.Embed(color=self.color, title='Bot Help')
        defaultEmbed.add_field(name='Bot Description', value='Description of the Bot')
        defaultEmbed.add_field(name='List of Commands', value='List of Commands')

        urbanEmbed = discord.Embed(color=self.color, title='Bot Help')
        urbanEmbed.add_field(name='Command Description', value='Description of the Command')
        urbanEmbed.add_field(name='Command Use', value='How to use the command')
        
        urbanRandomEmbed = discord.Embed(color=self.color, title='Bot Help')
        urbanRandomEmbed.add_field(name='Command Description', value='Description of the Command')
        urbanRandomEmbed.add_field(name='Command Use', value='How to use the command')
        
        nextDefEmbed = discord.Embed(color=self.color, title='Bot Help')
        nextDefEmbed.add_field(name='Command Description', value='Description of the Command')
        nextDefEmbed.add_field(name='Command Use', value='How to use the command')

        eightBallEmbed = discord.Embed(color=self.color, title='Bot Help')
        eightBallEmbed.add_field(name='Command Description', value='Description of the Command')
        eightBallEmbed.add_field(name='Command Use', value='How to use the command')
        
        helpEmbed = discord.Embed(color=self.color, title='Bot Help')
        helpEmbed.add_field(name='Command Description', value='Description of the Command')
        helpEmbed.add_field(name='Command Use', value='How to use the command')

        self.helpResponses = {'default': defaultEmbed,
                              'urban': urbanEmbed,
                              'urbanrandom': urbanRandomEmbed,
                              'nextdef': nextDefEmbed,
                              'help': helpEmbed,
                              '8ball': eightBallEmbed}

    @commands.command(name='help')
    async def help(self, ctx, *arg):
        if len(arg) == 1 and self.helpResponses[arg[0].lower()]:
            await ctx.send(embed=self.helpResponses[arg[0].lower()])
        else:
            await ctx.send(embed=self.helpResponses['default'])

