import discord
from discord.ext import commands

class TextParsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pTableColor = 0x078c50

    def searchPeriodicTable(self, content):
        # This regex doesn't work for words like fire, probably because it check in order?
        # pTableRegex = 'h[efgos]?|l[airuv]|b[aehikr]?|c[adeflmnorsu]?|n[abdehiop]?|o[gs]?|f[elmr]?|m[cdgnot]|a[cglmrstu]|s[bcegimnr]?|p[abdmortu]?|kr?|t[abcehilms]|v|z[nr]|g[ade]|r[abefghnu]|yb?|i[nr]?|xe|w|d[bsy]|e[sru]|u*'
        #
        # formattedContent = ''.join([x.lower() for x in content if x.lower() in 'abcdefghijklmnopqrstuvwxyz'])
        #
        # pTableString = ''.join([x.capitalize() for x in re.findall(pTableRegex, formattedContent)])
        #
        # if len(formattedContent) == len(pTableString):
        #     return pTableString
        pTable = {'h': ['', 'e', 'f', 'g', 'o', 's'],
                  'l': ['a', 'i', 'r', 'u', 'v'],
                  'b': ['', 'a', 'e', 'h', 'i', 'k', 'r'],
                  'c': ['', 'a', 'd', 'e', 'f', 'l', 'm', 'n', 'o', 'r', 's', 'u'],
                  'n': ['', 'a', 'b', 'd', 'e', 'h', 'i', 'o', 'p'],
                  'o': ['', 'g', 's'],
                  'f': ['', 'e', 'l', 'm', 'r'],
                  'm': ['c', 'd', 'g', 'n', 'o', 't'],
                  'a': ['c', 'g', 'l', 'm', 'r', 's', 't', 'u'],
                  's': ['', 'b', 'c', 'e', 'g', 'i', 'm', 'n', 'r'],
                  'p': ['', 'a', 'b', 'd', 'm', 'o', 'r', 't', 'u'],
                  'k': ['', 'r'],
                  't': ['a', 'b', 'c', 'e', 'h', 'i', 'l', 'm', 's'],
                  'v': [''],
                  'z': ['n', 'r'],
                  'g': ['a', 'd', 'e'],
                  'r': ['a', 'b', 'e', 'f', 'g', 'h', 'n', 'u'],
                  'y': ['', 'b'],
                  'i': ['', 'n', 'r'],
                  'x': ['e'],
                  'w': [''],
                  'd': ['b', 's', 'y'],
                  'e': ['s', 'r', 'y'],
                  'u': ['']}
        # Need to try a back tracking algorithm I think

        formattedContent = ''.join([x.lower() for x in content if x.lower() in 'abcdefghijklmnopqrstuvwxyz'])
        if len(formattedContent) == 0:
            return

        msgRewrite = []
        idx = 0
        back = False
        while idx < len(formattedContent):
            # check if two letter works, then check if one letter works if not go back
            if not back:
                curLetter = formattedContent[idx]
                if curLetter not in pTable:
                    if idx == 0:
                        return
                    back = True
                    continue
                if idx + 1 != len(formattedContent) and formattedContent[idx+1] in pTable[curLetter]:
                    msgRewrite.append(formattedContent[idx:idx + 2])
                    idx += 2
                    continue
                if '' in pTable[curLetter]:
                    msgRewrite.append(curLetter)
                    idx += 1
                    continue
                back = True
                continue
            else:
                idx -= len(msgRewrite[-1])
                prevVal = msgRewrite.pop(-1)
                if len(prevVal) == 2:
                    if '' in pTable[prevVal[0]]:
                        msgRewrite.append(prevVal[0])
                        idx += 1
                        back = False
                        continue
                    elif idx == 0:
                        return
                elif idx == 0:
                    return

        pTableString = ''.join([x.capitalize() for x in msgRewrite])

        return pTableString

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        pTableCheck = self.searchPeriodicTable(message.content)
        if pTableCheck:
            pTableResponse = 'Your message can be rewritten using Elements from the Periodic Table as:\n'
            pTableResponse += pTableCheck

            embed = discord.Embed(color=self.pTableColor)
            embed.add_field(name='Periodic Table', value=pTableResponse)
            await message.channel.send(embed=embed)

