import fastapi
from fastapi import Depends
from typing import Optional, List
from models.location import Location
from models.validation_error import ValidationError
from models.reports import Report, ReportSubmittal
from services.openweather_service import get_report_async
from services.report_service import get_reports, add_report

router = fastapi.APIRouter()

@router.get('/api/weather/{city}')
async def weather(
  loc: Location = Depends(),
  units :Optional[str] = 'metric'
  ):
  try:
    return await get_report_async(loc.city,loc.state,loc.country,units)
  except ValidationError as ve:
    return fastapi.Response(ve.error_msg, ve.status_code )
  except Exception as e:
    return fastapi.Response(content=str(e), status_code=500)

@router.get('/api/reports', name='all_reports')
async def reports_get() -> (List):
  return await get_reports()

@router.post('/api/reports', name='add_reports', status_code=201)
async def reports_post(report_submittal: ReportSubmittal) -> (Report):
  desc = report_submittal.desc
  loc = report_submittal.loc
  return await add_report(desc, loc)

  