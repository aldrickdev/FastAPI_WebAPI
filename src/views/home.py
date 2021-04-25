from starlette.requests import Request
from starlette.templating import Jinja2Templates
from services.report_service import  get_reports

import fastapi
router = fastapi.APIRouter()
templates = Jinja2Templates('templates')

@router.get('/')
async def index(request :Request):
  events = await get_reports()
  data = {'request' :request, 'events':events}
  return templates.TemplateResponse('home/index.html', data)

@router.get('/favicon.ico')
def favicon():
  return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')