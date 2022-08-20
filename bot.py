from itertools import cycle
import os
from random import choice
import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = os.environ.get("SECRET_TOKEN")
games = []
songs = [
    "xylo | afterlife [slowed down]",
    "Wanna break from the ads? X Quarto de Hotel - Hareton Salvanini",
    "Sleepwalk - New Stero Mix 2021"
]
titles = cycle([ ["playing", "a game of soccer"], ["watching", "a video on youtube"], ["listening", choice(songs)] ])

# --- BOT EVENTS ---

@bot.event
async def on_ready():
    print("Logged into bot 'The-Pickle-Helper'!")
    await appearance.start()

@tasks.loop(minutes=1)
async def appearance():
    status = next(titles)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType[status[0]], name=status[1]))

# --- BOT COMMANDS ---

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.command(aliases=["clear", "poof"])
async def purge(ctx, limit):
    await ctx.channel.purge(limit=(int(limit) + 1))
    messages_or_message = "messages" if int(limit) > 1 or int(limit) == 0 else "messages"
    messages = [
        f"I guess I'll have to search for the {messages_or_message} somewhere else...",
        f"{limit}_{messages_or_message} left the game.",
        f"{limit} {messages_or_message} went to go play an obby.",
        f"{limit} {messages_or_message} went to explore the endless wonders of No Man's Sky!"
    ]
    await ctx.send(choice(messages))

@bot.command(aliases=["game"])
async def randomgame(ctx):
    normal_games = [
        "Murder Mystery 2",
        "Flee the Facility",
        "Welcome to Bloxburg",
        "Eviction Notice",
        "Speed Run 4",
        "Impostor"
    ]
    horror_games = [
        "3008",
        "Daybreak",
        "Floppy's Playtime",
        "Apeirophobia",
        "The Mimic",
        "a dream you've had before"
    ]
    
    horrorGame = choice(horror_games)
    normalGame = choice(normal_games)
    
    prefixes = [
        { "HORROR": [
                f"Let's play a horrifyingly good game called {horrorGame}!",
                f"Have a great time! Looks like you'll be playing... {horrorGame}!",
                f"You're bound to scream while you play {horrorGame}!",
                f"I'm too scared there, the game is called {horrorGame}."
            ]
        },
        { "NORMAL": [
                f"{normalGame} is such a beautiful game!",
                f"Oh nice, enjoy your time while playing {normalGame}!",
                f"I'm jealous, guess you're playing {normalGame}!",
                f"Have a great time while you're in {normalGame}!"
            ]
        }
    ]
    
    gameChoice = choice([0, 1]) if True else False
    if gameChoice:
        await ctx.send(choice(prefixes[0]['HORROR']))
    else:
        await ctx.send(choice(prefixes[1]['NORMAL']))

if __name__ == "__main__":
    bot.run(TOKEN)