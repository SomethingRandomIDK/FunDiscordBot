import discord
import random
from discord.ext import commands

class EightBall(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.color = int(config['color'], 16)
        self.responses = config['responses']

    @commands.command(name='8ball')
    async def getResponse(self, ctx, *args):
        """When the 8ball command is called, it checks that there are
        arguments.  If there are arguments sends a message with a random
        response from the responses list
        """

        if len(args) == 0:
            embed = discord.Embed(color = self.color)
            embed.add_field(name='8ball Response',
                            value='Please ask a question')
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(color = self.color)
        embed.add_field(name='8ball Response',
                        value=random.choice(self.responses))
        await ctx.send(embed=embed)

