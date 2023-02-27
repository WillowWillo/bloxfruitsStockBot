import asyncio
import datetime

import discord
from discord.ext import commands

from bloxM import bloxM

# discord.Intents(guild_messages=True, messages=True, message_content=True)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = "Your Token Here"
c = '\n'.join(bloxM.currentStock())
l = '\n'.join(bloxM.lastStock())
p = '\n'.join(bloxM.pastStock())


@bot.command()
async def stock(ctx):
    await ctx.send(f"**Current Stock:**\n\n{c}\n"
                   f"\n**Last Stock:**\n\n{l}\n"
                   f"\n**Past Stock:**\n\n{p}\n")


# Only for debug.


'''

@commands.has_permissions(administrator=True)
@bot.command()
async def task(d):
    for taskk in asyncio.all_tasks():
        print(taskk)
        
'''


# Random command for test.


@commands.has_permissions(administrator=True)
@bot.command()
async def say(ctx, *, msg):
    try:
        await ctx.message.delete()
        await ctx.send(f"{msg}")
    except discord.ext.commands.errors.MissingPermissions:
        await ctx.channel.send("Sem permissão para executar o comando.")
    except Exception as E:
        await ctx.channel.send("Algum Erro Ocorreu, comunique a moderação.")
        print(ctx.guild)
        print(E)


# Random command for test.


@commands.has_permissions(administrator=True)
@bot.command()
async def clear(ctx, number):
    try:
        if str(number).isnumeric():
            await ctx.channel.purge(limit=int(number))
        else:
            await ctx.send("Bota um numeral amigão")
    except discord.ext.commands.errors.MissingPermissions:
        await ctx.channel.send("Sem permissão para executar o comando.")
    except Exception as E:
        await ctx.channel.send("Algum Erro Ocorreu, comunique a moderação.")
        print(ctx.guild)
        print(E)


# Random command for test.

@commands.has_permissions(administrator=True)
@bot.command()
async def clearBomb(ctx):
    try:
        for i in range(1, 5 + 1):
            await ctx.channel.purge(limit=int(100))
    except discord.ext.commands.errors.MissingPermissions:
        await ctx.channel.send("Sem permissão para executar o comando.")
    except Exception as E:
        await ctx.channel.send("Algum Erro Ocorreu, comunique a moderação.")
        print(ctx.guild)
        print(E)


async def daily():
    channel = bot.get_channel(0) # Type the channel ID of the channel that the daily messages are supposed to be send.
    data = datetime.date.today()
    listTime = [datetime.datetime.combine(data, datetime.time(7, 0)).replace(microsecond=0, second=0),
                datetime.datetime.combine(data, datetime.time(11, 0)).replace(microsecond=0, second=0),
                datetime.datetime.combine(data, datetime.time(15, 0)).replace(microsecond=0, second=0),
                datetime.datetime.combine(data, datetime.time(19, 0)).replace(microsecond=0, second=0),
                datetime.datetime.combine(data, datetime.time(23, 0)).replace(microsecond=0, second=0)]

    time_printed = False

    while True:
        await asyncio.sleep(5)
        now = datetime.datetime.now().replace(microsecond=0, second=0)
        if now in listTime and not time_printed:
            await channel.send(
                f"\n**Current Stock:**\n\n{c}\n"
                f"\n**Last Stock:**\n\n{l}\n"
                f"\n**Past Stock:**\n\n{p}\n")
            time_printed = True
        elif now not in listTime:
            time_printed = False


@bot.command()
async def voice(ctx):
    try:
        await ctx.channel.send(str(ctx.message.author.voice.channel))
        # await ctx.reply(str(discord.utils.get(bot.voice_clients, guild=ctx.guild)))
        await ctx.reply(str(bot.voice_clients))

    except AttributeError:
        await ctx.reply("Você não está em um canal de voz bobinho.")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    myTask = asyncio.Task(daily())
    await asyncio.sleep(3)
    await bot.change_presence(activity=discord.Game(name="Blox Fruits"))


bot.run(token)
