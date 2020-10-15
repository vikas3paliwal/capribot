import discord
from discord.ext import commands
import os
# from config import token

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def pic(channel, file):
    filename = 'images/'+file+'.jpeg'
    await channel.send(file=discord.File(filename))


token = os.environ['discord_token']
client.run(token)