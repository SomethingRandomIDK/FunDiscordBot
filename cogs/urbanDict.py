import discord
import requests
from discord.ext import commands

class UrbanDict(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randList = []
        self.selDefList = []
        self.defListLen = 0
        self.selWord = None
        self.color = 0xad2424

    def generateResponse(self, wordEntry, embed=None):
        if not embed:
            embed = discord.Embed(color=self.color)
            embed.add_field(name='Word:', value=wordEntry['word'], inline=False)

        definition = wordEntry['definition'].replace('[', '').replace(']', '')
        example = wordEntry['example'].replace('[', '').replace(']', '')
        embed.add_field(name='Definition:', value=definition, inline=False)
        embed.add_field(name='Example:', value=example, inline=False)
        
        return embed

    @commands.command(name='urbanrandom')
    async def randomWord(self, ctx):
        if len(self.randList) == 0:
            self.randList = requests.get('https://api.urbandictionary.com/v0/random').json()['list']
        embed = self.generateResponse(self.randList[0])
        await ctx.send(embed=embed)
        self.randList.pop(0)

    @commands.command(name='urban')
    async def selectedWord(self, ctx, *, arg=None):
        if not arg:
            embed = discord.Embed(color=self.color)
            embed.add_field(name='Urban Dictionary', value='Please enter a word/phrase to search')
            await ctx.send(embed=embed)
            return

        url = 'https://api.urbandictionary.com/v0/define?term='
        url += arg.lower().strip().replace(' ', '&')

        self.selDefList = requests.get(url).json()['list']
        self.defListLen = len(self.selDefList)
        self.selWord = arg
        if self.defListLen == 0:
            message = f'{arg} was not found in the Urban Dictionary'
            embed = discord.Embed(color=self.color)
            embed.add_field(name='Urban Dictionary', value=message, inline=False)
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(color=self.color)
        message = f'*Defintion 1 of {self.defListLen}*'
        embed.add_field(name='Number of Definitions:', value=message, inline=False)
        embed.add_field(name='Word:', value=arg.capitalize(), inline=False)
        embed = self.generateResponse(self.selDefList[0], embed=embed)
        await ctx.send(embed=embed)
        self.selDefList.pop(0)

    @commands.command(name='nextdef')
    async def getNextDefintion(self, ctx):
        if len(self.selDefList) == 0:
            message = f'There are no additional definitions available please check [the official Urban Dictionary website](https://www.urbandictionary.com) for more defintions'
            embed = discord.Embed(color=self.color)
            embed.add_field(name='Urban Dictionary', value=message, inline=False)
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(color=self.color)
        curDef = self.defListLen - len(self.selDefList) + 1
        message = f'*Definition {curDef} of {self.defListLen}*'
        embed.add_field(name='Number of Definitions:', value=message, inline=False)
        embed.add_field(name='Word:', value=self.selWord.capitalize(), inline=False)
        embed = self.generateResponse(self.selDefList[0], embed=embed)
        await ctx.send(embed=embed)
        self.selDefList.pop(0)

