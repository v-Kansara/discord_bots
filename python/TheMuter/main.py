import discord
import os
import random
import asyncio

from discord.ext import commands
from discord.utils import get
from keep_alive import keep_alive

client = discord.Client()
Token = os.getenv('Token')
color = 0x0bcad4

@client.event
async def ch_pr():
  await client.wait_until_ready()

  statuses = [f"Mute Boi",
  f"on {len(client.guilds)} servers", "L + Ratio + Bozo"]

  while not client.is_closed():
    status = random.choice(statuses)
    await client.change_presence(
    activity=discord.Activity(type=discord.ActivityType.playing, name=status))
    await asyncio.sleep(10)


client.loop.create_task(ch_pr())

@client.event
async def on_message(message):
  if "cap" in message.content.lower():
    embed=discord.Embed(title="Warning", description="Stop saying CAP!!")
    embed.set_author(name="The Muter",  icon_url="https://images.ctfassets.net/lzny33ho1g45/when-to-mute-video-calls-p-img/b3fb904f03d4aca4f805bfdffbd455f4/file.png?w=1520&fm=jpg&q=30&fit=thumb&h=760")
    embed.add_field(name="Reason", value="User's message contained cap", inline=False)
    embed.set_footer(text="Literally Get Perma-Muted.")
    await message.channel.send(embed=embed)

  if "bruh" in message.content.lower():
    embed=discord.Embed(title="Warning", description="Stop saying BRUH!!")
    embed.set_author(name="The Muter",  icon_url="https://images.ctfassets.net/lzny33ho1g45/when-to-mute-video-calls-p-img/b3fb904f03d4aca4f805bfdffbd455f4/file.png?w=1520&fm=jpg&q=30&fit=thumb&h=760")
    embed.add_field(name="Reason", value="User's message contained bruh", inline=False)
    embed.set_footer(text="I WILL LITERALLY BAN YOU!!")
    await message.channel.send(embed=embed)

  if "imagine" in message.content.lower():
    embed=discord.Embed(title="Warning", description="Stop saying IMAGINE!!")
    embed.set_author(name="The Muter",  icon_url="https://images.ctfassets.net/lzny33ho1g45/when-to-mute-video-calls-p-img/b3fb904f03d4aca4f805bfdffbd455f4/file.png?w=1520&fm=jpg&q=30&fit=thumb&h=760")
    embed.add_field(name="Reason", value="User's message contained imagine", inline=False)
    embed.set_footer(text="Imagine saying Imagine. Nerd.")
    await message.channel.send(embed=embed)

  if "magine" in message.content.lower():
    embed=discord.Embed(title="Warning", description="Stop saying MAGINE!!")
    embed.set_author(name="The Muter",  icon_url="https://images.ctfassets.net/lzny33ho1g45/when-to-mute-video-calls-p-img/b3fb904f03d4aca4f805bfdffbd455f4/file.png?w=1520&fm=jpg&q=30&fit=thumb&h=760")
    embed.add_field(name="Reason", value="User's message contained magine", inline=False)
    embed.set_footer(text="What a rip-off.")
    await message.channel.send(embed=embed)

keep_alive()
client.run(Token)