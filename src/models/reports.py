import datetime
from typing import Optional
from pydantic import BaseModel
from models.location import Location

class ReportSubmittal(BaseModel):
  desc :str
  loc :Location

class Report(ReportSubmittal):
  id :str
  created_date :Optional[datetime.datetime]