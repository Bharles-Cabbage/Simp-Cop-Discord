import os
import discord

from random import randint
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
botToken = os.getenv("DISCORD_TOKEN")


# List of simping words
words = ["erotic", "cute", "beautiful", "sexy", "hot", "lovely", "beauty", "hawt", "kawai", "pretty"]

# List of messages to be sent
messages = ["Simping has been found, and {0.author.mention} is the culprit!!", "Ahh, there you are. {0.author.mention} aka. Simp Lord!"]

# List of nicknames to be given
nicknames = ["I'm a simp", "Simp Lord", "I lick monitors watching Poki", "Your bathwater makes me wet", "I drool for your feet pics", "I'm a Simp and not ashamed"]

# Client refers to the bot
bot = discord.Client()

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
    msgList = msg.content.replace("."," ").strip().lower().split(" ")

    # Find for a complement in the message sent
    if any(word in words for word in msgList):

        # Random nickname
        nickname = nicknames[randint(0, len(nicknames)-1)]

        # Change their nickname in server 
        await msg.author.edit(nick=nickname)
        
        # Select a message to be sent, and mention the user that simped
        random_message = messages[randint(0, len(messages)-1)].format(msg)

        # Send warning
        await msg.channel.send(random_message)

bot.run(botToken)
