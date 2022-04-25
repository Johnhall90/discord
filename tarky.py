#!/usr/bin/python3
import discord
import os
import json
from dotenv import load_dotenv
from discord.ext import commands
from os.path import exists
from tabulate import tabulate

load_dotenv()
TOKEN = os.getenv('TARKY_TOKEN')

bot = discord.Client()

bot = commands.Bot(command_prefix='.') #Define the command prefix. Any command starts with '!' to call the bot

bot.remove_command("help")

leaderboard = {}
leaderboard_fn = '/home/jhall/discord/leaderboard.json'



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.help'))
    # Recognize global leaderboard
    global leaderboard

    # Only load the leaderboard if the file exists
    if exists(leaderboard_fn):
        with open(leaderboard_fn, 'r') as leaderboard_file:
            leaderboard = json.load(leaderboard_file)

async def help(ctx):
    em = discord.Embed(title = "Text Channel Commands", description = "Use the prefix '!' to invoke commands so you feel like big hacker boy.", color = discord.Color.green())
    em.add_field(name = '.tk', value = 'Record team kills')
    em.add_field(name = '.stat', value = 'TK Leaderboard')
    em.set_thumbnail(url="https://i.imgur.com/TJfM6Q8.jpg")
    em.set_author(name="Monke",url="https://i.imgur.com/TJfM6Q8.jpg",icon_url="https://i.imgur.com/TJfM6Q8.jpg")
    await ctx.send(embed = em)

@bot.command()
async def tk(ctx, killer_name: discord.Member = None, killed_name: discord.Member = None):
    if killer_name and killed_name:
        await ctx.send(f"Uh oh!! {killer_name.mention} fucking teamkilled {killed_name.mention}! That's another one for the books <:GOTTEM:852236935836991488>")
        await ctx.send(file=discord.File('/home/jhall/images/trust_noone.jpg'))

        killer = str(killer_name.id)
        killed = str(killed_name.id)

        # Recognize global leaderboard
        global leaderboard

        # Adds the killer to the leaderboard if they're not in it
        if killer not in leaderboard:
            leaderboard[killer] = {}

        # Add to the dictionary if the killed person already exists
        if killed in leaderboard[killer]:
            leaderboard[killer][killed] += 1
        # Create a new dictionary instance if the killed doesn't exist
        else:
            leaderboard[killer][killed] = 1

        with open(leaderboard_fn, 'w') as leaderboard_file:
            leaderboard_file.write(json.dumps(leaderboard, indent=4))

async def getPlayersKilled():
    global leaderboard

    playersKilled = {}

    for killer in leaderboard:

        # Create a new key in dictionary to hold sum
        playersKilled[killer] = 0

        # Adds the total number of kills up
        for killed in leaderboard[killer]:

            playersKilled[killer] += leaderboard[killer][killed]

    playersKilled = dict(sorted(playersKilled.items(), key=lambda item: item[1], reverse=True))

    toReturn = []

    for killer in playersKilled:
        user = await bot.fetch_user(int(killer))
        toReturn.append([user.name,playersKilled[killer]])

    print(tabulate(toReturn, headers=["Teamkiller", "Kills"], tablefmt="pretty"))
    return tabulate(toReturn, headers=["Teamkiller", "Kills"], tablefmt="pretty")

async def getKilledPlayers() -> dict:

    global leaderboard

    killedPlayers = {}

    # Loops through the people that the killers killed
    for killer in leaderboard:

        for killed in leaderboard[killer]:

            if killed not in killedPlayers:
                killedPlayers[killed] = 0

            killedPlayers[killed] += leaderboard[killer][killed]

    killedPlayers = dict(sorted(killedPlayers.items(), key=lambda item: item[1], reverse=True))

    toReturn = []

    for killed in killedPlayers:
        user = await bot.fetch_user(int(killed))
        toReturn.append([user.name,killedPlayers[killed]])

    print(tabulate(toReturn, headers=["Victim", "Deaths"], tablefmt="fancy_grid"))

    return tabulate(toReturn, headers=["Victim", "Deaths"], tablefmt="pretty")

@bot.command()
async def stats(ctx):
    output_killed = await getPlayersKilled()
    output_killer = await getKilledPlayers()
    lb = discord.Embed(title = "Teamkiller Hall of Fame", description = "Leaderboard for Tarkov teamkills. Below shows who killed the most, and who got killed the most.", color = discord.Color.red())
    lb.add_field(name = 'Most TK\'s', value = output_killed)
    lb.add_field(name = 'Most times TK\'d', value = output_killer)
    await ctx.send(embed = lb)         
bot.run(TOKEN)