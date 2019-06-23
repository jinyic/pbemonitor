import os
from datetime import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=os.environ["cmd_prefix"])


def create_embed(title, message):
    embed = discord.Embed(
        title=title,
        type="rich",
        description=message,
        timestamp=datetime.utcnow(),
        colour=64154,
    )
    embed.set_footer(text="By  Jin Yi")
    return embed


@bot.event
async def on_ready():
    print(bot.user.name + " Launched")
    print("By Jin Yi")
    print("-" * 20)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def start(ctx):
    await ctx.send("pong")


@bot.command()
async def embed(ctx):
    await ctx.send(embed=create_embed("Test Notification", "PBE live!"))


bot.run(os.environ["token"])
