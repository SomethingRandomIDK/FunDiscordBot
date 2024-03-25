from datetime import time
import discord
import requests
from discord.ext import commands, tasks

urlSearch = 'https://images-api.nasa.gov/search'
urlAPOD = 'https://api.nasa.gov/planetary/apod'
APODtime = [time(hour=21, minute=49)]

class Nasa(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.color = int(config['color'], 16)
        self.searchResults = None

        self.picOfDay.start()

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

    @tasks.loop(time=APODtime)
    async def picOfDay(self):
        print('calling this')
        params = {'api_key': 'DEMO_KEY',
                  'thumbs': 1}
        daily = requests.get(urlAPOD, params=params).json()
        picUrl = None
        if 'hdurl' in daily:
            picUrl = daily['hdurl']
        else:
            picUrl = daily['url']
        picTitle = daily['title']

        embed = discord.Embed(color=self.color,
                              title='Astronomy Picture of The Day')
        embed.set_image(url=picUrl)
        embed.add_field(name='Image Title:', value=picTitle)

        for x in self.bot.guilds:
            print('this works')
            if x.system_channel is not None:
                await x.system_channel.send(embed=embed)

