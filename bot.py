import discord
from discord.ext import commands
from config import token

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def homie(channel):
    await channel.send(file=discord.File('images/homie.jpeg'))

client.run(token)