import fastapi
from starlette.routing import Host
import uvicorn
import httpx 

api = fastapi.FastAPI()

@api.get('/')
def index():
  return "Hello"

if __name__ == '__main__':
  uvicorn.run(api, port=8001, host='127.0.0.1')