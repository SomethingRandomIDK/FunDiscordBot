import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        """Generates embeds for each command in the bot and loads all the
        embeds into a dictionary
        """

        self.bot = bot
        self.color = 0xe8e805

        defaultEmbed = discord.Embed(color=self.color, title='Bot Help')
        lCommands = '`urban`\n'
        lCommands += '`urbanrandom`\n'
        lCommands += '`nextdef`\n'
        lCommands += '`8ball`\n'
        lCommands += 'You can use `?help [command]` for more information about each of these commands'
        defaultEmbed.add_field(name='List of Commands', value=lCommands)

        urbanEmbed = discord.Embed(color=self.color, title='Bot Help')
        urbanDescription = "This searches the [Urban Dictionary](https://www.urbandictionary.com) for a word or phrase"
        urbanEmbed.add_field(name='Urban Description',
                             value=urbanDescription,
                             inline=False)
        urbanUse = '`?urban [word/phrase]`\nThe `[word/phrase]` should be replaced by what you are searching for'
        urbanEmbed.add_field(name='Urban Use',
                             value=urbanUse,
                             inline=False)
        
        urbanRandomEmbed = discord.Embed(color=self.color, title='Bot Help')
        urbanRandomDescription = "This gets a random word from [Urban Dictionary](https://www.urbandictionary.com)"
        urbanRandomEmbed.add_field(name='Command Description',
                                   value=urbanRandomDescription,
                                   inline=False)
        urbanRandomEmbed.add_field(name='Command Use',
                                   value='`?urbanrandom`',
                                   inline=False)
        
        nextDefEmbed = discord.Embed(color=self.color, title='Bot Help')
        nextDefDescription = 'This gets an alternate defintion for the last word searched using the urban command'
        nextDefEmbed.add_field(name='NextDef Description',
                               value=nextDefDescription,
                               inline=False)
        nextDefEmbed.add_field(name='NextDef Use',
                               value='`?nextdef`',
                               inline=False)

        eightBallEmbed = discord.Embed(color=self.color, title='Bot Help')
        eightDescription = 'This answers questions asked like an 8ball would'
        eightBallEmbed.add_field(name='8ball Description',
                                 value=eightDescription,
                                 inline=False)
        eightUse = '`?8ball [question]`\nThe `[question]` should be replaced by what you are asking'
        eightBallEmbed.add_field(name='8ball Use',
                                 value=eightUse,
                                 inline=False)
        
        self.helpResponses = {'default': defaultEmbed,
                              'urban': urbanEmbed,
                              'urbanrandom': urbanRandomEmbed,
                              'nextdef': nextDefEmbed,
                              '8ball': eightBallEmbed}

    @commands.command(name='help')
    async def help(self, ctx, *arg):
        """Displays a help message. If help is called with a valid command as
        an argument, it displays the help for that specific command.
        Otherwise the default help message is displayed.
        """

        if len(arg) == 1 and self.helpResponses[arg[0].lower()]:
            await ctx.send(embed=self.helpResponses[arg[0].lower()])
        else:
            await ctx.send(embed=self.helpResponses['default'])

