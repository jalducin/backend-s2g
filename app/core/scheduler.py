from apscheduler.schedulers.background import BackgroundScheduler
from app.models.fake_db import stations

def change_status():
    for s in stations:
        s["status"] = "activo" if s["status"] == "inactivo" else "inactivo"

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(change_status, "interval", minutes=1)
    scheduler.start()