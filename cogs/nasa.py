import discord
import requests
from discord.ext import commands

urlSearch = 'https://images-api.nasa.gov/search'

class Nasa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x7aa9f5
        self.searchResults = None

    @commands.command(name='nasaSearch')
    async def nasaSearch(self, ctx, *args):
        search = ' '.join(args)
        searchParams = {'q': search,
                        'media_type': 'image'}
        images = requests.get(urlSearch, params=searchParams).json()
        self.searchResults = images['collection']['items']
        embed = discord.Embed(color=self.color, title='NASA Image Search')
        embed.set_image(url=self.searchResults[0]['links'][0]['href'])
        embed.add_field(name='Image Title:',
                        value=self.searchResults[0]['data'][0]['title'])
        await ctx.send(embed=embed)
        self.searchResults.pop(0)

    @commands.command(name='nextImg')
    async def nextImg(self, ctx):
        embed = discord.Embed(color=self.color, title='NASA Image Search')
        embed.set_image(url=self.searchResults[0]['links'][0]['href'])
        embed.add_field(name='Image Title:',
                        value=self.searchResults[0]['data'][0]['title'])
        await ctx.send(embed=embed)
        self.searchResults.pop(0)

