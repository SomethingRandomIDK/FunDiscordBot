import re
from discord.ext import commands

class TextParsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def searchPeriodicTable(self, content):
        pTableRegex = 'h[efgos]?|l[airuv]|b[aehikr]?|c[adeflmnorsu]?|n[abdehiop]?|o[gs]?|f[elmr]?|m[cdgnot]|a[cglmrstu]|s[bcegimnr]?|p[abdmortu]?|kr?|t[abcehilms]|v|z[nr]|g[ade]|r[abefghnu]|yb?|i[nr]?|xe|w|d[bsy]|e[sru]|u*'

        formattedContent = ''.join([x.lower() for x in content if x.lower() in 'abcdefghijklmnopqrstuvwxyz'])

        pTableString = ''.join([x.capitalize() for x in re.findall(pTableRegex, formattedContent)])

        if len(formattedContent) == len(pTableString):
            return pTableString

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        pTableCheck = self.searchPeriodicTable(message.content)
        if pTableCheck:
            pTableResponse = 'Your message can be rewritten using Elements from the Periodic Table as:\n'
            pTableResponse += pTableCheck
            await message.channel.send(pTableResponse)

