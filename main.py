import os
import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
botToken = os.getenv("DISCORD_TOKEN")

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
    if msg.content in ["cute", "beautiful", "sed"]:
        await msg.channel.send("SIMPPPP DETECTEDDD")


bot.run(botToken)
