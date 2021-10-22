import discord

import subprocess

from discord.ext import commands

client = commands.Bot(command_prefix=';', intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Pronto')

@client.command()
async def processo(ctx, *, processo):
    subprocess.Popen(processo.split(), shell=True)

@client.command()
async def response(ctx):
    await ctx.send(f'> **Ok**\n> `{client.latency * 1000}ms`')

client.run('OTAwNDg3MDMyNzk3Nzk0Mzk2.YXCB5g.7JBnduHGoATXfmAsfHaIc1BuljU')