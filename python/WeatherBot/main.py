import discord
import os
import requests
import json

from keep_alive import keep_alive
from weather import *

client = discord.Client()

command_prefix = 'w.'
Token = os.getenv('Token_Weather')
Api_Key = os.getenv('Api_Key')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}[location]'))

@client.event
async def on_message(message):
  if message.author != client.user and message.content.startswith(command_prefix):
    location = message.content.replace(command_prefix, '').lower()
    if len(location) >= 1:
      # Get Weather Data
      url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={Api_Key}&units=imperial'
      data = json.loads(requests.get(url).content)
      try:
        data = parse_data(data)
        await message.channel.send(embed=weather_message(data, location))
      except KeyError:
        await message.channel.send(embed=error_message(location))

keep_alive()
client.run(Token)