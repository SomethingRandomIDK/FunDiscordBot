import discord
from discord.ext import commands

class TextParsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pTableColor = 0x078c50

    def searchPeriodicTable(self, content):
        """Checks if content can be rewritten using Symbols from the
        Periodic Table. If possible, outputs the rewritten content as a string
        """

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

        formattedContent = ''.join([x.lower() for x in content if x.lower() in 'abcdefghijklmnopqrstuvwxyz'])
        if len(formattedContent) == 0:
            return

        msgRewrite = []
        idx = 0
        back = False
        while idx < len(formattedContent):
            if not back:
                curLetter = formattedContent[idx]
                if curLetter not in pTable:
                    if idx == 0:
                        return
                    back = True
                elif idx + 1 != len(formattedContent) and formattedContent[idx+1] in pTable[curLetter]:
                    msgRewrite.append(formattedContent[idx:idx + 2])
                    idx += 2
                elif '' in pTable[curLetter]:
                    msgRewrite.append(curLetter)
                    idx += 1
                else:
                    back = True
            else:
                if idx == 0:
                    return
                idx -= len(msgRewrite[-1])
                prevVal = msgRewrite.pop(-1)
                if len(prevVal) == 2:
                    if '' in pTable[prevVal[0]]:
                        msgRewrite.append(prevVal[0])
                        idx += 1
                        back = False
                    elif idx == 0:
                        return
                elif idx == 0:
                    return

        pTableString = ''.join([x.capitalize() for x in msgRewrite])

        return pTableString

    @commands.Cog.listener()
    async def on_message(self, message):
        """Tries to rewrite all messages using symbols from the periodic table.
        If possible reponds with the rewritten message.
        """

        if message.author.bot:
            return
        pTableCheck = self.searchPeriodicTable(message.content)
        if pTableCheck:
            pTableResponse = 'Your message can be rewritten using Elements from the Periodic Table as:\n'
            pTableResponse += pTableCheck

            embed = discord.Embed(color=self.pTableColor)
            embed.add_field(name='Periodic Table', value=pTableResponse)
            await message.channel.send(embed=embed)

