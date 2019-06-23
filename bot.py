import os
import time
from datetime import datetime
import requests
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=os.environ["cmd_prefix"])
monitoring = False


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
    await bot.change_presence(activity=discord.Activity(
        name="butterflies",
        type=discord.ActivityType.watching,
        start=datetime.utcnow()))
    print(bot.user.name + " Launched")
    print("By Jin Yi")
    print("-" * 20)


@bot.command()
async def ping(ctx):
    await ctx.send(embed=create_embed("PBE Monitor", "Pong!"))


@bot.command()
async def start(ctx):
    global monitoring
    monitoring = True
    # update presence to indicate monitor is on
    await bot.change_presence(activity=discord.Activity(
        name="the PBE server status",
        type=discord.ActivityType.watching,
        start=datetime.utcnow()))
    while monitoring:
        r = requests.get("https://status.pbe.leagueoflegends.com/shards/pbe")
        if r.status_code == 200 and r.json()["services"][0]["status"] != "offline":
            await ctx.send(embed=create_embed("PBE LIVE!", "Sign in quickly!"))
        time.sleep(int(os.environ["delay"]))


@bot.command()
async def stop(ctx):
    global monitoring
    monitoring = False
    await bot.change_presence(activity=discord.Activity(
        name="butterflies",
        type=discord.ActivityType.watching,
        start=datetime.utcnow()))

bot.run(os.environ["token"])
