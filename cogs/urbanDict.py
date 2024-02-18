import requests
from discord.ext import commands

class UrbanDict(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randList = []
        self.selDefList = []
        self.defListLen = 0
        self.selWord = None

    def generateResponse(self, wordEntry, word=None):
        response = ''

        if not word:
            word = wordEntry['word']
        response += f'**Word:** {word}\n'

        definition = wordEntry['definition'].replace('[', '').replace(']', '')
        example = wordEntry['example'].replace('[', '').replace(']', '')
        response += f'**Definition:**\n{definition}\n'
        response += f'**Example:**\n{example}\n'
        
        return response

    @commands.command(name='urbanrandom')
    async def randomWord(self, ctx):
        if len(self.randList) == 0:
            self.randList = requests.get('https://api.urbandictionary.com/v0/random').json()['list']
        message = self.generateResponse(self.randList[0])
        await ctx.send(message)
        self.randList.pop(0)

    @commands.command(name='urban')
    async def selectedWord(self, ctx, *, arg):
        url = 'https://api.urbandictionary.com/v0/define?term='
        url += arg.lower().strip().replace(' ', '&')

        self.selDefList = requests.get(url).json()['list']
        self.defListLen = len(self.selDefList)
        self.selWord = arg
        if self.defListLen == 0:
            await ctx.send(f'{arg} was not found in the Urban Dictionary')
            return

        message = f'*Defintion 1 of {self.defListLen}*\n'
        message += self.generateResponse(self.selDefList[0], arg)
        await ctx.send(message)
        self.selDefList.pop(0)

    @commands.command(name='nextdef')
    async def getNextDefintion(self, ctx):
        if len(self.selDefList) == 0:
            await ctx.send(f'There are no additional definitions available please check [the official Urban Dictionary website](https://www.urbandictionary.com) for more defintions')
            return

        curDef = self.defListLen - len(self.selDefList) + 1
        message = f'*Definition {curDef} of {self.defListLen}*\n'
        message += self.generateResponse(self.selDefList[0], self.selWord)
        await ctx.send(message)
        self.selDefList.pop(0)

