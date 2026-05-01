import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Ready event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Miku is ready to sing! 🎤")

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 💙")

# Chat command
@bot.command()
async def miku(ctx, *, message):
    responses = [
        "Ehh?! That's interesting! 🎶",
        "Hehe~ tell me more! 💙",
        "Yayyy! I love chatting with you! ✨"
    ]
    await ctx.send(random.choice(responses))

# Sing command
@bot.command()
async def sing(ctx):
    lyrics = [
        "La la la~ 🎤✨",
        "Singing makes everything better! 💙",
        "Feel the music in your heart! 🎶"
    ]
    await ctx.send(random.choice(lyrics))

# Coin flip game
@bot.command()
async def coinflip(ctx):
    await ctx.send(random.choice(["Heads!", "Tails!"]))

# Run bot
bot.run("8665621150:AAE1AYh-ZNs0md9mvB3X8RxgUGpZbeef9XE")
