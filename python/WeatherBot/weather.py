import discord

color = 0xeb2d02
key_features = {
  'temp': 'Temperature :white_sun_rain_cloud:',
  'feels_like': 'Feels Like',
  'humidity': 'Humidity',
  'temp_max': 'Maximum Temperature :sunny:',
  'temp_min': 'Minimum Temperature :snowflake:',
}

def parse_data(data):
  data = data['main']
  del data['pressure']
  return data

def weather_message(data, location):
  location = location.title()
  message = discord.Embed(title=f'{location} Weather', description=f'Here is the weather data for {location}.', color=color)
  for key in data:
    message.add_field(name=key_features[key], value=str(data[key]), inline=False)
  return message

def error_message(location):
  location = location.title()
  return discord.Embed(title='Error', description=f'There was an error retrieving weather data for {location}.', color=color)