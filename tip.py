#!/usr/bin/python3
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
import lights

load_dotenv()
TOKEN = os.getenv('TIP_TOKEN')

bot = commands.Bot(command_prefix='!') #Define the command prefix. Any command starts with '!' to call the bot

satellite = [                          #Array of file locations to satellite gifs
              '/home/jhall/images/satt1.gif',
              '/home/jhall/images/satt2.gif',
              '/home/jhall/images/satt3.gif',
              '/home/jhall/images/satt4.gif',
              '/home/jhall/images/satt5.gif'  
            ]

bangalore = [                          #Array of file locations to bangalore audio
              '/home/jhall/sounds/lifeline.mp3',
              '/home/jhall/sounds/steel.wav',
              '/home/jhall/sounds/smoke.wav',
              '/home/jhall/sounds/iron.wav',
              '/home/jhall/sounds/foxtrot.wav',
              '/home/jhall/sounds/ambush.wav'  
            ]

bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('!help you stinkers'))
    

#Tip command to invoke math on tipping at restaraunts
@bot.command()
async def tip(ctx, arg):
    #Do the math on tip percentages
    amount = float(arg)
    fifteen = "%.2f" % (amount * 0.15)
    fifteen = float(fifteen)
    fifteen_total = "%.2f" % (amount + fifteen)
    fifteen_total = float(fifteen_total)
    twenty = "%.2f" % (amount * 0.20)
    twenty = float(twenty)
    twenty_total = "%.2f" % (amount + twenty)
    twenty_total = float(twenty_total)

    channel = ctx.channel

    #Send the percentages and the totals with both percentages
    await channel.send('With a bill of $' + arg + ' here is the tip breakdown:')
    await channel.send('15%: $' + str(fifteen) + ' for a total of $' + str(fifteen_total))
    await channel.send('20%: $' + str(twenty) + ' for a total of $' + str(twenty_total))

#Who command that sends a message and gif in the same message
@bot.command()
async def who(ctx):
    channel = ctx.channel
    await channel.send('Who asked?? Any askers???' , file=discord.File('/home/jhall/images/modcheck.gif'))

#Find command that outputs 2 messages and a gif
@bot.command()
async def find(ctx):
    channel = ctx.channel
    await channel.send('One moment...searching the globe for askers...' , file=discord.File(random.choice(satellite))) #choose random file location of gifs
    await channel.send('NASA couldn\'t find any askers...')

@bot.command()
async def lou(ctx):
    channel = ctx.channel
    await channel.send(file=discord.File('/home/jhall/images/loustrW.png'))

@bot.command()
async def help(ctx):
    em = discord.Embed(title = "Text Channel Commands", description = "Use the prefix '!' to invoke commands so you feel like big hacker boy.", color = discord.Color.green())
    em.add_field(name = '!who', value = 'Who asked?')
    em.add_field(name = '!lou', value = 'funni emote')
    em.add_field(name = '!tip', value = '!tip <value> to calculate tip/total')
    em.add_field(name = '!mark', value = 'Markov bot is always listening')
    em.add_field(name = '!find', value = 'Call on the NASA satellite infrastructure via Andrew', inline=False)
    em.set_thumbnail(url="https://i.imgur.com/TJfM6Q8.jpg")
    em.set_author(name="Monke",url="https://i.imgur.com/TJfM6Q8.jpg",icon_url="https://i.imgur.com/TJfM6Q8.jpg")
    await ctx.send(embed = em)

    em2 = discord.Embed(title = "Voice Channel Commands", description = "These commands require you to be in a voice channel.", color = discord.Color.red())
    em2.add_field(name = '!fart', value = 'fart')
    em2.add_field(name = '!monke', value = 'monke')
    em2.add_field(name = '!bang', value = 'worse legend')
    em2.add_field(name = '!stop', value = 'monke leave')
    em2.add_field(name = '!bugs', value = 'I\'ve been here before')
    em2.add_field(name = '!dws', value = 'Double-wide surprise')
    em2.add_field(name = '!mmm', value = 'You got a tight little man bussy')
    em2.set_thumbnail(url="https://i.imgur.com/TJfM6Q8.jpg")
    em2.set_author(name="Monke",url="https://i.imgur.com/TJfM6Q8.jpg",icon_url="https://i.imgur.com/TJfM6Q8.jpg")
    await ctx.send(embed = em2)

@bot.command()
async def fart(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=('/home/jhall/sounds/wet-fart_1.mp3')))
    time.sleep(1.25)
    await server.voice_client.disconnect()

@bot.command()
async def monke(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=('/home/jhall/sounds/UH OH.mp3')))

@bot.command()
async def ankha(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=('/home/jhall/sounds/ankha.mp3')))
    time.sleep(100.00)
    await server.voice_client.disconnect()

@bot.command()
async def verysecret(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=('/home/jhall/sounds/vent.mp3')))
    time.sleep(2.00)
    await server.voice_client.disconnect()

@bot.command()
async def bugs(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=('/home/jhall/sounds/bugs.mp3')))
    time.sleep(5.00)
    await server.voice_client.disconnect()

@bot.command()
async def dws(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=('/home/jhall/sounds/dws.mp3')))
    time.sleep(6.00)
    await server.voice_client.disconnect()

@bot.command()
async def mmm(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=('/home/jhall/sounds/mmm.mp3')))
    time.sleep(7.00)
    await server.voice_client.disconnect()

@bot.command()
async def bang(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=(random.choice(bangalore))))
    time.sleep(4.35)
    await server.voice_client.disconnect()

@bot.command()
async def stop(ctx):
    await ctx.guild.voice_client.disconnect()

@bot.command()
async def dn(ctx):
    channel = ctx.channel
    dn_file = open("/home/jhall/discord/counter.txt","r+")
    dn_counter = dn_file.readline()
    counter = int(dn_counter)
    counter += 1
    dn_counter = str(counter)
    print(dn_counter)
    
    dn_file.seek(0)
    dn_file.write(dn_counter)
    dn_file.truncate()
    dn_file.close()
    await channel.send("DEEZ NUTS <:GOTTEM:852236935836991488> | successfully gottemed " + dn_counter + " beeshes")

@bot.command()
async def color(ctx, arg):
    print(arg)
    lights.changeColor(arg)

bot.run(TOKEN)