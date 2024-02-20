import discord
import random
from discord.ext import commands

responses = ['It is certain',
             'It is decidedly so',
             'Without a doubt',
             'Yes definitely',
             'You may rely on it',
             'As I see it, yes',
             'Most likely',
             'Outlook good',
             'Yes',
             'Signs point to yes',
             'Reply hazy, try again',
             'Ask again later',
             'Better not tell you now',
             'Cannot predict now',
             'Concentrate and ask again',
             'Don\'t count on it',
             'My reply is no',
             'My sources say no',
             'Outlook not so good',
             'Very doubtful']

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x4b0082

    @commands.command(name='8ball')
    async def getResponse(self, ctx):
        embed = discord.Embed(color = self.color)
        embed.add_field(name='8ball Response', value=random.choice(responses))
        await ctx.send(embed=embed)

