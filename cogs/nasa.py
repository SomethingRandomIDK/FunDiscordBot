from datetime import time
import discord
import requests
from discord.ext import commands, tasks

urlSearch = 'https://images-api.nasa.gov/search'
urlAPOD = 'https://api.nasa.gov/planetary/apod'
APODtime = [time(hour=18, minute=53, second=45)]

class Nasa(commands.Cog):
    def __init__(self, bot, config, apiKey):
        self.bot = bot
        self.color = int(config['color'], 16)
        self.searchResults = None
        self.key = apiKey

        self.picOfDay.start()

    @commands.command(name='nasa')
    async def nasaSearch(self, ctx, *args):
        search = ' '.join(args)
        searchParams = {'q': search,
                        'media_type': 'image'}
        images = requests.get(urlSearch, params=searchParams).json()

        embed = discord.Embed(color=self.color, title='NASA Image Search')
        if len(images['collection']['items']) == 0:
            embed.add_field(name='No Results',
                            value='No results were found from your search. Try searching something else.')
        else:
            self.searchResults = images['collection']['items']
            embed.set_image(url=self.searchResults[0]['links'][0]['href'])
            embed.add_field(name='Image Title:',
                            value=self.searchResults[0]['data'][0]['title'])
            self.searchResults.pop(0)

        await ctx.send(embed=embed)

    @commands.command(name='nextimg')
    async def nextImg(self, ctx):
        embed = discord.Embed(color=self.color, title='NASA Image Search')
        if len(self.searchResults) == 0:
            embed.add_field(name='End of Results',
                            value='No additional results were found from your search. Try searching something else.')
        else:
            embed.set_image(url=self.searchResults[0]['links'][0]['href'])
            embed.add_field(name='Image Title:',
                            value=self.searchResults[0]['data'][0]['title'])
            self.searchResults.pop(0)

        await ctx.send(embed=embed)

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


