from typing import Optional 
import httpx
from infastructure.weather_cache import get_weather,set_weather


api_key :Optional[str] = None

async def get_report_async(
  city :str,
  state :Optional[str],
  country :str,
  units :str
  )->(dict):
  """
  Takes in the city, state, country, units and checks the cache to see if an updated forecast is available\n
  if not available in cache, get an up to date forecast from the api and update the cache\n
  Returns a dict of the forecast
  """
  # forecast: dict = weather_cache.get_weather(city, state, country, units)
  # if forecast:
  #   return forecast

  # same as above
  # checks to see if forecast is already in the cache
  forecast: dict
  if forecast := get_weather(city,state,country,units):
    return forecast

  if state:
    q = f"{city},{state},{country}"
  else:
    q = f"{city},{country}"

  key = api_key
  url = f"http://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}"

  async with httpx.AsyncClient() as client:
    resp = await client.get(url)
    resp.raise_for_status()

  data = resp.json()
  forecast = data['main']

  set_weather(city, state, country, units, forecast)

  return forecast
