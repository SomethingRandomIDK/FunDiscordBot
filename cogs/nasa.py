import discord
import requests
from discord.ext import commands

urlSearch = 'https://images-api.nasa.gov/search'

class Nasa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x7aa9f5

    @commands.command(name='nasaSearch')
    async def nasaSearch(self, ctx, *args):
        search = ' '.join(args)
        searchParams = {'q': search,
                        'media_type': 'image'}
        images = requests.get(urlSearch, params=searchParams).json()
        embed = discord.Embed(color=self.color, title='NASA Image Search')
        embed.set_image(url=images['collection']['items'][0]['links'][0]['href'])
        await ctx.send(embed=embed)

