# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('OK_TOKEN')

bot = discord.Client()

filth = ["oK.", "ok.", "Ok", "oK", "Ok.", "OK", "OK.", "0k", "0k.", "0K", "0K.", "!vent"]
not_filth = ["ok", "ok?", "ok..."]
emojis = ['🆗', '🙂']
count = 0
vent = "!verysecret"
sussy = "ifunny"

@bot.event
async def on_message(message):
        cringe = message.content
        if cringe in filth: #checks if shitty ok spelling is in the message
            if vent in cringe:
                await message.channel.purge(limit=1) #delete the message
                channel = message.channel #sets to current channel message was sent in
                await channel.send('||<Redacted>||'+message.author.mention) #@ the user
            elif sussy in cringe:
                await message.channel.purge(limit=1) #delete the message
                channel = message.channel #sets to current channel message was sent in
                await channel.send('Fuck you, no cringey ifunny links in here'+message.author.mention) #@ the user
            else:
                await message.channel.purge(limit=1) #delete the message
                channel = message.channel #sets to current channel message was sent in
                await channel.send('Fuck you '+message.author.mention) #@ the user
                await channel.send(file=discord.File('/home/jhall/images/tenor2.gif')) #send knuckles gif
        elif cringe in not_filth: #checks for the only correct spelling of ok
            channel = message.channel
            if message.author == bot.user:
                pass
            else:
                global count
                count += 1
                print(count)
                if cringe == "ok?":
                    await channel.send('ok...?')
                    await channel.send('???')
                elif cringe == "ok...":
                    await channel.send('?')
                    await channel.send('ok...bro??')
                elif count == 3:
                    channel = message.channel
                    em = discord.Embed(title = "seriously stop", description = "bro STOP seriously saying ok", color = discord.Color.orange())
                    em.add_field(name = '.', value = 'DUDE stop', inline=False)
                    em.add_field(name = '.', value = '....?', inline=False)
                    em.add_field(name = '.', value = 'ok', inline=False)
                    em.set_thumbnail(url="https://i.imgur.com/TJfM6Q8.jpg")
                    em.set_author(name="Monke",url="https://i.imgur.com/TJfM6Q8.jpg",icon_url="https://i.imgur.com/TJfM6Q8.jpg")
                    await channel.send(embed = em)
                    count = 0
                else:   
                    await channel.send('ok')
                    for emoji in emojis: #loops through the emojis to react with
                        await message.add_reaction(emoji) #reacts to the message with emojis
bot.run(TOKEN)