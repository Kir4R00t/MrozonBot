import os
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
BOT_TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Startup
@bot.event
async def on_ready():
    # Main bot guild (which is a serer of two ppl :v)
    global guild
    for guild in bot.guilds:
        if guild.name == guild:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    try:
        print("Synced commands: \n")
        synced = await bot.tree.sync()
        for x in synced:
            print(f'{x}\n')
        if synced is None:
            print(f'{x} is not synced\n')

    except Exception as error:
        print(error)

    print(f"Active discord members in {guild}:")
    for member in guild.members:
        print(f'{member.name}\n')

# Commands



bot.run(BOT_TOKEN)