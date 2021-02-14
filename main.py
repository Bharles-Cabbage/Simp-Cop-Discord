# Built in modules
import os
from random import randint

# Third Party libs and modules
import discord
from dotenv import load_dotenv

# Local import
from sentences import phrases
from words import words

# Load environment variables from .env file
load_dotenv()
botToken = os.getenv("DISCORD_TOKEN")

# Client refers to the bot
bot = discord.Client()

# List of messages to be sent
messages = ["Simping has been found, and {0.author.mention} is the culprit!!", "Ahh, there you are. {0.author.mention} aka. Simp Lord!"]

# List of nicknames to be given
nicknames = ["I'm a simp", "Simp Lord", "I lick monitors watching Poki", "Your bathwater makes me wet", "I drool for your feet pics", "I'm a Simp and not ashamed"]

# Helper function to replace multiple characters 
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)

    return  mainString


@bot.event
async def on_ready():
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
            # PRINT THE SERVER'S ID AND NAME.
            print(f"- {guild.id} (name: {guild.name})")

            # INCREMENTS THE GUILD COUNTER.
            guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Simp cop Bot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(msg):
    
    simp = False

    # Find for a complement in the message sent
    for i in phrases:
        if i in msg.content.lower():
            simp = True

    #Replace symbols with white spaces, change case, then split into list of words
    msgList = replaceMultiple(msg.content, [".", ",", "|", "#", "?"], " ").strip().lower().split(" ")

    if simp or any(word in words for word in msgList):
        # Random nickname
        nickname = nicknames[randint(0, len(nicknames)-1)]

        # Change their nickname in server 
        await msg.author.edit(nick=nickname)
        
        # Select a message to be sent, and mention the user that simped
        random_message = messages[randint(0, len(messages)-1)].format(msg)

        # Send warning
        await msg.channel.send(random_message)

bot.run(botToken)
