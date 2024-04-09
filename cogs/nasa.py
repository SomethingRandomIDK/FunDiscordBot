from datetime import datetime
import json
import discord
import requests
from discord.ext import commands, tasks

urlSearch = 'https://images-api.nasa.gov/search'
urlAPOD = 'https://api.nasa.gov/planetary/apod'


f = open('config.json')
nasaConfig = json.load(f)['cogs']['nasa']
f.close()

APODtime = []
APODtime.append(datetime.strptime(nasaConfig['APODtime'], '%H:%M:%S').time())

class Nasa(commands.Cog):
    def __init__(self, bot, config, apiKey):
        self.bot = bot
        self.color = int(config['color'], 16)
        self.searchResults = None
        self.key = apiKey

        if config['APOD']:
            self.picOfDay.start()
            

        self.help = {'commands':
                     {'nasa':
                      {'usage': '`nasa [word/phrase]`\nThe `[word/phrase]` should be replaced by what you are searching for',
                       'description': 'Searches NASA\'s Image Database an returns the closest result'},
                      'nextimg':
                      {'usage': '`nextimg`',
                       'description': 'Returns the next closest result for the previous nasa search'}},
                     'features':
                     {'Astronomy Picture of the Day': 'Sends NASA\'s Astronomy Picture of the Day on a daily basis'}}

    @commands.command(name='nasa')
    async def nasaSearch(self, ctx, *args):
        '''Submits a search request for only images matching args to the
        NASA Image/Video API and then sends the first result
        '''
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
        '''Sends the next result returned from last search made with the nasa
        command
        '''
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
        '''Sends NASA Astronomy Picture of the Day in all server's system
        channel at the time specified by APODtime
        '''
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


