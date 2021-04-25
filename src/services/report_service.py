import datetime
from typing import List
from models.location import Location
from models.reports import Report
import uuid

__reports :List[Report] = []

async def get_reports() -> (List):

  # Would be an async call 
  return list(__reports)

async def add_report(desc :str, loc :Location) -> (Report):
  now = datetime.datetime.now()
  report = Report(id = str(uuid.uuid4()), desc = desc, loc = loc, created_date = now)

  # Simulating savign to database
  # would be async call here
  __reports.append(report)
  __reports.sort(key=lambda r: r.created_date, reverse=True)

  return report