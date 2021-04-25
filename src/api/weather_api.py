import fastapi
from fastapi import Depends
from typing import Optional
from models.location import Location
from models.validation_error import ValidationError
from services.openweather_service import get_report_async

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
  