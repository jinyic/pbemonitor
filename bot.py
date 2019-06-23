import os
from datetime import datetime
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


@bot.command()
async def embed(ctx):
    time = str(datetime.utcnow())
    json_time = time.replace(" ", "T")
    payload = {
        "embeds": [
            {
                "color": 64154,
                "description": "PBE Live!",
                "title": "Test Notification",
                "timestamp": json_time,
                "url": "",
                "image": {"url": ""},
                "thumbnail": {},
                "footer": {"text": "By Jin Yi", "icon_url": ""}
            }
        ]
    }
    await ctx.send(payload)


bot.run(os.environ["token"])
