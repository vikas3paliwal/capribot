import discord
from discord.ext import commands
from config import token

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def pic(channel, file):
    filename = 'images/'+file
    await channel.send(file=discord.File(filename))

client.run(token)