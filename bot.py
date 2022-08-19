import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = os.environ.get("SECRET_TOKEN")

@bot.event
async def on_ready():
    print("Logged into bot 'The-Pickle-Helper'!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

if __name__ == "__main__":
    bot.run(TOKEN)