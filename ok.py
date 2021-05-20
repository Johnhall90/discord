# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

filth = ["oK.", "ok.", "Ok", "oK", "Ok.", "OK", "OK.", "0k", "0k.", "0K", "0K."]
not_filth = ["ok", "ok?"]
emojis = ['🆗', '🙂']

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
        cringe = message.content
        if cringe in filth: #checks if shitty ok spelling is in the message
            await message.channel.purge(limit=1) #delete the message
            channel = message.channel #sets to current channel message was sent in
            await channel.send('Fuck you '+message.author.mention) #@ the user
            await channel.send(file=discord.File('home/jhall/tenor.gif')) #send knuckles gif
        elif cringe in not_filth: #checks for the only correct spelling of ok
            channel = message.channel
            if message.author == bot.user:
                pass
            else: 
                if cringe == "ok?":
                    await channel.send('ok...?')
                    await channel.send('???')
                else:   
                    await channel.send('ok')
                    for emoji in emojis: #loops through the emojis to react with
                     await message.add_reaction(emoji) #reacts to the message with emojis
bot.run(TOKEN)