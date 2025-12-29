import uuid
from datetime import datetime
from app.models import Event
from app.schemas import EventRequest

EVENT_STORE = []

def process_event(event: EventRequest):
    event_obj = Event(
        event_id=str(uuid.uuid4()),
        event_type=event.event_type,
        source=event.source,
        payload=event.payload,
        timestamp=datetime.utcnow()
    )

    EVENT_STORE.append(event_obj)

    return {
        "event_id": event_obj.event_id
    }
