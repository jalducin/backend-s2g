from fastapi import FastAPI
from app.core.scheduler import start_scheduler
from app.routers.auth import router as auth_router
from app.routers.station import router as station_router
from app.routers.stats import router as stats_router
from app.routers.scheduler import router as scheduler_router

app = FastAPI(title="S2G Backend API")

# Registrar todos los routers
app.include_router(auth_router)
app.include_router(station_router)
app.include_router(stats_router)
app.include_router(scheduler_router)

@app.on_event("startup")
def startup_event():
    # Inicia el APScheduler
    start_scheduler()
