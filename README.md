# Discord Bot
A Discord Bot with various features to make Discord servers more fun and interesting.

---
# Installation
The setup for the bot is fairly simple by following these steps.

1. Follow the steps on [this website](https://discordpy.readthedocs.io/en/stable/discord.html) to create your discord bot.
2. Create a .env file based on the .env.example file, copying your discord bot Token from the previous step into the file.
3. Open a terminal and run the following commands:

    ```
    git clone https://github.com/SomethingRandomIDK/FunDiscordBot.git
    ```
    ```
    cd FunDiscordBot
    ```
    ```
    pip install -r requirements.txt
    ```
    ```
    python3 bot.py
    ```

---
# Features
## Help
This bot has a basic help function with the default output being a list of commands available. As well as indepth help available for each of the commands with another help command.

**help**

This command gives the list of available commands

<img src="./images/help.png" alt="help">

**help** [command]

This command gives more detailed instructions about how to use the command

<img src="./images/helpcommand.png" alt="help [command]">

## Urban Dictionary
Has a set of 3 commands to lookup words from [Urban Dictionary](https://www.urbandictionary.com)

**urbanrandom**

This command gets a random word and shows the word, defintion, and example

<img src="./images/urbanrandom.png" alt="urbanrandom">

**urban** [word/phrase]

This command gets the definition and example of the specified word

<img src="./images/urban.png" alt="urban [word/phrase]">

**nextdef**

This command gets an alternate defintion and example for the most recently searched word

<img src="./images/nextdef.png" alt="nextdef">

## 8 Ball
This emulates the toy 8 ball.  You can ask the bot's 8 ball a question and it will give a random answer.

**8ball** [question]

This commands generates a random answer for your question that can align with either yes, no, or maybe.

<img src="./images/8ball.png" alt="8ball">

## Periodic Table Detector
Detects if the users message can be rewritten using the Elements Symbols from the Periodic Table, it ignores everything in the message except for letters.  If a message can be rewritten using the Periodic Table, the bot shows how the message would be rewritten.

<img src="./images/ptable.png" alt="Periodic Table Detector">
