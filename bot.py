import os
import random
import discord
import requests
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

def chance_to_respond(chance): # Chance == % of success
    throw = random.randint(1, 100)
    if throw <= chance:
        return True
    else:
        return False

# - Reactions
@bot.event
async def on_message(message):

    responses = {'aquoos': f'Bro really just said: {message.content} :skull:',
                'bawanisko': 'smacznego makaronu :lick:',
                'd4rq': ':lick:'
    }
    
    toxic_responses = ['sam spierdalaj',
                       'twoja stara',
                       ':skull:',
                       'no chyba ty',
                       'masz małego siura',
                       'twój stary :fire:',
                       'ruchał cie Dawid :lick:',
                       'Kijaszek z ciebie :cold_face:']

    if message.author.name in responses:
        if chance_to_respond(20):
            await message.channel.send(responses[message.author.name])
            
    if bot.user.mentioned_in(message):
        if message.author.name == 'kirar00t':
            await message.channel.send('At your command my liege')
        else:
            await message.channel.send(toxic_responses[random.randint(0, len(toxic_responses))]) # Roll a random response
    
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
