# bot.py
import os
import random #random class used to pick random gif from array

import discord
from dotenv import load_dotenv
from discord.ext import commands

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

bot.run(TOKEN)