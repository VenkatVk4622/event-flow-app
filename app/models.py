from dataclasses import dataclass
from typing import Dict
from datetime import datetime

@dataclass
class Event:
    event_id: str
    event_type: str
    source: str
    payload: Dict
    timestamp: datetime
