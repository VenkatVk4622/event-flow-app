from fastapi import APIRouter
from app.schemas import EventRequest
from app.services import process_event

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/")
def ingest_event(event: EventRequest):
    result = process_event(event)
    return {
        "message": "Event processed successfully",
        "event_id": result["event_id"]
    }
