import os
# import discord
from discord.ext import commands
# import subprocess

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.command()
async def join(ctx):
    vc = ctx.author.voice.channel
    await vc.connect()


@client.command()
async def bye(ctx):
    await ctx.voice_client.disconnect()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(API_KEY)
