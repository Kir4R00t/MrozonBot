import os
import requests
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
BOT_TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# - Startup
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# - Reactions
@bot.event
async def on_message(message):
    if message.author.name == 'aquoos':
        roll = random.randint(1, 5)
        if roll == 1:
            await message.channel.send(f'Bro really just said: {message.content} :skull:')
    if bot.user.mentioned_in(message):
        if message.author.name == 'kirar00t':
            await message.channel.send('At your command my liege')
        else:
            roll = random.randint(1,5)
            if roll == 1:
                await message.channel.send('sam spierdalaj')
            elif roll == 2:
                await message.channel.send('twoja stara')
            elif roll == 3:
                await message.channel.send(':skull:')
            elif roll == 4:
                await message.channel.send('no chyba ty')
            elif roll == 5:
                await message.channel.send('masz małego siura')
            
# - Commands
# Test
@bot.tree.command(name="test", description="test command")
async def test(interaction: discord.Interaction):
    guild = interaction.guild
    await interaction.response.send_message(f"You are on a server named: {guild}", ephemeral=False)

# CATSSS
@bot.tree.command(name="gibcat", description="Get a random image of a cat :3")
async def gibcat(interaction: discord.Interaction):
    load_dotenv('token.env')
    api_key = os.getenv('CAT_API')
    url = f"https://api.thecatapi.com/v1/images/search?&api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cat_photo_url = (data[0]['url'])
        if data:
            await interaction.response.send_message(cat_photo_url, ephemeral=False)
        else:
            await interaction.response.send_message("No data from API", ephemeral=False)
    else:
        await interaction.response.send_message(f"API ERROR: {response.status_code}", ephemeral=False)


bot.run(BOT_TOKEN)