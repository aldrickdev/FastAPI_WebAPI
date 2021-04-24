import fastapi
import uvicorn
from pathlib import Path
import json
from services import openweather_service
from starlette.staticfiles import StaticFiles
from views import home
from api import weather_api

api = fastapi.FastAPI()

def configure():
  configure_routing()
  configure_api_key()

def configure_api_key():
  file = Path('../settings.json').absolute()
  if not file.exists():
    print("settings.json not found in root of project")
    raise Exception("settings.json not found in root of project")
  with open('../settings.json') as fin:
    settings = json.load(fin)
    openweather_service.api_key = settings.get('api_key')

def configure_routing():
  api.mount('/static', StaticFiles(directory='static'), name='static')
  api.include_router(home.router)
  api.include_router(weather_api.router)

if __name__ == '__main__':
  configure()
  uvicorn.run(api, port=8001, host='127.0.0.1')
else:
  configure()