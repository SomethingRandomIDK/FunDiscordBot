import requests
from discord.ext import commands

class UrbanDict(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randList = []

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

