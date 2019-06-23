import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=os.environ["cmd_prefix"])


@bot.event
async def on_ready():
    print(bot.user.name + " Launched")
    print("By Jin Yi")
    print("-" * 20)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


bot.run(os.environ["token"])
