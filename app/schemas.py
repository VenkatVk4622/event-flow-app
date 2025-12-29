from pydantic import BaseModel
from typing import Dict

class EventRequest(BaseModel):
    event_type: str
    source: str
    payload: Dict
