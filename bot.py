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

    # did it in dict
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
    embed = discord.Embed(
        title="Test Notification",
        type="rich",
        description="PBE live!",
        timestamp=datetime.utcnow(),
        colour=64154,
    )
    embed.set_footer(text="By  Jin Yi")
    await ctx.send(embed=embed)


bot.run(os.environ["token"])
