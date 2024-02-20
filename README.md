# DiscordBot
A Discord Bot with various features to make Discord servers more fun and interesting.

---
# Installation
The setup for the bot is fairly simple by following these steps.

1. Follow the steps on [this website](https://discordpy.readthedocs.io/en/stable/discord.html) to create your discord bot.
2. Create a .env file based on the .env.example file, copying your discord bot Token from the previous step into the file.
3. Open a terminal and run the following commands:
4. `git clone https://github.com/SomethingRandomIDK/GeneralDiscordBot.git`
5. `cd GeneralDiscordBot`
6. `pip install -r requirements.txt`
7. `python3 bot.py`

---
# Features
## Urban Dictionary
Has a set of 3 commands to lookup words from [Urban Dictionary](https://www.urbandictionary.com)

**urbanrandom**

This command gets a random word and shows the word, defintion, and example

**urban** [word/phrase]

This command gets the definition and example of the specified word

**nextdef**

This command gets an alternate defintion and example for the most recently searched word

## 8Ball

## Periodic Table Detector
Detects if the users message can be rewritten using the Elements Symbols from the Periodic Table, it ignores everything in the message except for letters.  If a message can be rewritten using the Periodic Table, the bot shows how the message would be rewritten.
