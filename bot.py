import discord
import asyncio
from discord.ext import commands

import random

from _config import TOKEN

startup_extensions = ['inventory', 'rpg', 'battle']

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description='RPG Bot')

@bot.event
async def on_ready():
    print('Logged in as: {0}\n(ID: {0.id})'.format(bot.user))

@bot.event
async def on_member_join(member):
    server = member.server
    txt = 'Welcome {0.mention} to {1.name}'
    await client.send_message(server, txt.format(member, server))

@bot.command()
async def load(extension_name : str):
    """Loads an extension"""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("***py\n{}: {}\n***".format(type(e).__name__, str(e)))
        return
    await bot.say('{} loaded.'.format(extension_name))

@bot.command()
async def unload(extension_name: str):
    """Unload an extension."""
    bot.unload_extension(extension_name)
    await bot.say('{} unloaded.'.format(extension_name))


if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}'.format(extension))
            print('{}: {}'.format(type(e).__name__, e))

    bot.run(TOKEN)
