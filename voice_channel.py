import os
import discord
from discord.ext import commands
# import subprocess

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']  # raise KeyError if not exist

client = commands.Bot(command_prefix='!hey ')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.command(aliases=["yo"])
async def join(ctx):
    """"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send('Please join voice channel at first.')
        return

    await voice_state.channel.connect()
    print('Connected to {0.channel.name}'.format(voice_state))


@client.command()
async def bye(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    await ctx.send('disconnected.')


@client.command()
async def play(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send('I don\'t connect to any voice channel.')
        return

    if not ctx.message.attachments:
        await ctx.send('give me a music file')

    await ctx.message.attachments[0].save("tmp.mp3")

    source = discord.FFmpegPCMAudio("tmp.mp3")

    voice_client.play(source)

    await ctx.send('listen it!')


client.run(API_KEY)
