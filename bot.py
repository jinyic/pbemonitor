import os
import time
from datetime import datetime
import requests
import discord
from discord.ext import commands, tasks

CMD_PREFIX = os.environ["cmd_prefix"]
OFFLINE_DELAY = os.environ["off_delay"]
ONLINE_DELAY = os.environ["on_delay"]
TOKEN = os.environ["token"]


bot = commands.Bot(command_prefix=CMD_PREFIX)

state = ""
monitor_channel = None
monitoring = False


async def create_embed(title, message):
    embed = discord.Embed(
        title=title,
        type="rich",
        description=message,
        timestamp=datetime.utcnow(),
        colour=64154,
    )
    embed.set_footer(text="By  Jin Yi")
    return embed


async def set_presence(message):
    await bot.change_presence(activity=discord.Activity(
        name=message,
        type=discord.ActivityType.watching,
        start=datetime.utcnow()))


@bot.event
async def on_ready():
    global state
    # get current state
    r = requests.get("https://status.pbe.leagueoflegends.com/shards/pbe")
    state = r.json()["services"][0]["status"]

    # set presence to show pbe server status
    await set_presence(f"PBE | {CMD_PREFIX}start")

    print(bot.user.name + " Launched")
    print("By Jin Yi")
    print("-" * 20)


@bot.command()
async def ping(ctx):
    print(monitor.current_loop)
    await ctx.send(embed=await create_embed("PBE Monitor", "Pong!"))


@bot.command()
async def start(ctx):
    global state, monitor_channel, monitoring
    # check if it is on a loop
    if monitoring:
        await ctx.send(embed=await create_embed("PBE Monitor", "Bot is already monitoring"))
        return

    monitoring = True
    monitor_channel = ctx.channel
    await ctx.send(embed=await create_embed("PBE Monitor", "Bot is now watching the PBE server status"))
    await set_presence(f"PBE | Status: {state.upper()}")
    await monitor.start()


@bot.command()
async def stop(ctx):
    global monitoring
    if not monitoring:
        await ctx.send(embed=await create_embed("PBE Monitor", "Bot is already stopped"))
        return

    monitor.stop()
    monitoring = False
    await ctx.send(embed=await create_embed("PBE Monitor", "Bot stopped monitoring"))
    await set_presence(f"PBE | {CMD_PREFIX}start")


@tasks.loop(seconds=10)
async def monitor():
    global state, monitor_channel
    # get server status
    r = requests.get("https://status.pbe.leagueoflegends.com/shards/pbe")
    new_state = r.json()["services"][0]["status"]

    if r.status_code == 200:
        if new_state != state:
            state = new_state
            if state == "online":
                await monitor_channel.send(embed=await create_embed("PBE LIVE!", "Sign in quickly!"))
                await set_presence(f"PBE | Status: {state.upper()}")

            else:
                await monitor_channel.send(embed=await create_embed("PBE Server Update", "Server is offline"))
                await set_presence(f"PBE | Status: {state.upper()}")

        # when server is online, long delay, offline short delay
        if state == "online":
            monitor.change_interval(seconds=int(ONLINE_DELAY))
        else:
            monitor.change_interval(seconds=int(OFFLINE_DELAY))

    # sleep, status_code != 200 probably is a ban
    else:
        monitor.change_interval(seconds=10)

if __name__ == '__main__':
    bot.run(TOKEN)
