import datetime
from typing import Optional, Tuple

__cache = {}
lifetime_in_hours = 1.0

def get_weather(
  city: str, 
  state: Optional[str], 
  country: str, 
  units: str
  ) -> (Optional[dict]):
  """
  Checks the cache for the weather\n
  if the weather exist in the cache and has been there for less than lifetime_in_hours
  \tReturns the weather in dict
  else
  \tReturns None
  """
  # Creates the key as a tuple
  key = __create_key(city, state, country, units)

  # Checks to see if that key already exist in cache
  data: dict = __cache.get(key)
  if not data:
    return None

  # checks to see how long since this key has been updated
  last = data['time']
  dt = datetime.datetime.now() - last

  # checks to see if the time since updating is smaller than the lifetime_in_hours, then return the value from cache
  if dt / datetime.timedelta(minutes=60) < lifetime_in_hours:
    return data['value']

  # delete the KVP from cache and return None
  del __cache[key]
  return None

def set_weather(
    city: str,
    state: str,
    country: str,
    units: str,
    value: dict
  ) -> (None):
  """
  Creates the Key Value Pair, enters it into cache and clears out of date Key Value Pairs in the cache
  """
  # creates a key out of the city, state, country, units
  key = __create_key(city, state, country, units)
  # create the value pair for the key 
  data = {
    'time': datetime.datetime.now(),
    'value': value
  }

  # enteres the KVP into cache
  __cache[key] = data

  __clean_out_of_date()

def __create_key(
    city: str,
    state: str,
    country: str,
    units: str
  ) -> (Tuple[str, str, str, str]):
  """
  Takes the city, state, country and units\n
  Returns a tuple with city, state, country and units without leading and trailing whitespace and lowercase
  """
  # Checks to see if the required values are entered
  if not city or not country or not units:
    raise Exception("City, country and units are required")
  
  # Sets state to empty string if state is not None
  if not state:
    state = ""
  
  # returns the city, state, country and units without leading and trailing whitespace and lowercase
  return (
    city.strip().lower(), 
    state.strip().lower(),
    country.strip().lower(),
    units.strip().lower()
    )

def __clean_out_of_date():
  """
  Checks each KVP in __cache and deletes it if its been cached for longer than lifetime_in_hours
  """
  # gets each KVP in __cache as a list of tuples (key, value)
  for key, data in list(__cache.items()): 
      # checks if the KVP has been in cache for longer than lifetime_in_hours, if so deletes that KVP
      dt = datetime.datetime.now() - data.get('time')
      if dt / datetime.timedelta(minutes=60) > lifetime_in_hours:
          del __cache[key]






