# bot.py
import os
import random #random class used to pick random gif from array
import time
from typing import get_args
from warnings import resetwarnings
import discord
from discord import message
from discord.enums import _create_value_cls
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('FEET_TOKEN')

bot = commands.Bot(command_prefix='?') #Define the command prefix. Any command starts with '!' to call the bot

bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('!help'))

#Who command that sends a message and gif in the same message
@bot.command()
async def feet(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send('Ladies, if you have any feet(please say yes please say yes) please send them to me for a quick rating (and nothing cringe at all)' +ctx.author.mention)

@bot.command()
async def nff(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send('Attention all women, please send feet (and toes). No father figure required.')

@bot.command()
async def normal(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send(ctx.author.mention+' is normal, well-adjusted, hinged, mentally sound, reformed, and not cringe. Ladies, please DM him.')

@bot.command()
async def love(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send(ctx.author.mention+' loves and respects all women now. Do NOT DM them, you will be blocked.')

@bot.command()
async def ratio(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send('L + ratio\'d + ugly feet + gets no bitches')

@bot.command()
async def blissful(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send(file=discord.File('/home/jhall/images/blissful.png'))

@bot.command()
async def reason(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send(file=discord.File('/home/jhall/images/ban.png'))

@bot.command()
async def wink(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send('( *.-)')

@bot.command()
async def floppa(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send(file=discord.File('/home/jhall/images/floppa.gif'))

@bot.command()
async def chat(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send(file=discord.File('/home/jhall/images/chat.png'))

@bot.command()
async def reason2(ctx):
    await ctx.channel.purge(limit=1)
    channel = ctx.channel
    await channel.send(file=discord.File('/home/jhall/images/reason2.png'))

@bot.command()
async def help(ctx):
    em = discord.Embed(title = "Text Channel Commands", description = "Use the prefix '?' to invoke commands so you feel like big hacker boy.", color = discord.Color.green())
    em.add_field(name = '?feet', value = 'Send feet')
    em.add_field(name = '?nff', value = 'No father figured required')
    em.add_field(name = '?normal', value = 'Normal and well adjusted btw')
    em.add_field(name = '?love', value = 'Love and respect women')
    em.add_field(name = '?ratio', value = 'Ratio\'d')
    em.add_field(name = '?blissful', value = 'Blissful reformed')
    em.add_field(name = '?reason', value = 'retard')
    em.add_field(name = '?wink', value = '( *.-)')
    em.add_field(name = '?floppa', value = 'Pass the floppa')
    em.set_thumbnail(url="https://i.kym-cdn.com/photos/images/facebook/001/851/676/75e.png")
    em.set_author(name="Normal and Well Adjusted",url="https://i.kym-cdn.com/photos/images/facebook/001/851/676/75e.png",icon_url="https://i.kym-cdn.com/photos/images/facebook/001/851/676/75e.png")
    await ctx.send(embed = em)

    # em2 = discord.Embed(title = "Voice Channel Commands", description = "These commands require you to be in a voice channel.", color = discord.Color.red())
    # em2.add_field(name = '!fart', value = 'fart')
    # em2.add_field(name = '!monke', value = 'monke')
    # em2.add_field(name = '!bang', value = 'worse legend')
    # em2.add_field(name = '!stop', value = 'monke leave')
    # em2.add_field(name = '!bugs', value = 'I\'ve been here before')
    # em2.add_field(name = '!dws', value = 'Double-wide surprise')
    # em2.add_field(name = '!mmm', value = 'You got a tight little man bussy')
    # em2.set_thumbnail(url="https://i.kym-cdn.com/photos/images/facebook/001/851/676/75e.png")
    # em2.set_author(name="Normal and Well Adjusted",url="https://i.kym-cdn.com/photos/images/facebook/001/851/676/75e.png",icon_url="https://i.kym-cdn.com/photos/images/facebook/001/851/676/75e.png")
    # await ctx.send(embed = em2)

bot.run(TOKEN)