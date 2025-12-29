from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Event Flow App",
    description="Real-time event ingestion service",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "Event Flow App is running"}
