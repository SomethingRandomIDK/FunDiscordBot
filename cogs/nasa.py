from datetime import time
import discord
import requests
from discord.ext import commands, tasks

urlSearch = 'https://images-api.nasa.gov/search'
urlAPOD = 'https://api.nasa.gov/planetary/apod'
APODtime = [time(hour=17, minute=56)]

class Nasa(commands.Cog):
    def __init__(self, bot, config, apiKey):
        self.bot = bot
        self.color = int(config['color'], 16)
        self.searchResults = None
        self.key = apiKey

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
        params = {'api_key': self.key,
                  'thumbs': True}
        daily = requests.get(urlAPOD, params=params).json()

        embed = discord.Embed(color=self.color,
                              title='Astronomy Picture of The Day')

        if daily['media_type'] == 'image':
            picUrl = None
            if 'hdurl' in daily:
                picUrl = daily['hdurl']
            else:
                picUrl = daily['url']
            picTitle = daily['title']

            embed.add_field(name='Image Title:', value=picTitle)
            embed.set_image(url=picUrl)

            for x in self.bot.guilds:
                if x.system_channel is not None:
                    await x.system_channel.send(embed=embed)
        else:
            vidUrl = daily['url']
            
            embed.add_field(name='Video Title:', value=daily['title'])
            embed.set_thumbnail(url=daily['thumbnail_url'])
            
            for x in self.bot.guilds:
                if x.system_channel is not None:
                    await x.system_channel.send(embed=embed)
                    await x.system_channel.send(f'||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||{vidUrl}')


