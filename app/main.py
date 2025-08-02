from fastapi import FastAPI, Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload

from app.database import engine, SessionLocal, Base
from app.logger import logger
from app.models import Region
from app.models_db import RegionDB, WardDB, PlotDB

app = FastAPI(title="WardMonitor", version="1.0")

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    regions = db.query(RegionDB).options(
        joinedload(RegionDB.wards).joinedload(WardDB.plots)
    ).all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "regions": regions})


@app.post("/ward-update")
async def receive_region(region: Region, db: Session = Depends(get_db)):
    logger.info(f"Received data for region: {region.region_name}")

    if "Unknown" in region.region_name:
        return {"status": "nok", "received": region.region_name}

    # Try to get existing region
    db_region = db.query(RegionDB).filter(RegionDB.region_name == region.region_name).first()
    if not db_region:
        db_region = RegionDB(region_name=region.region_name)
        db.add(db_region)
        db.commit()
        db.refresh(db_region)

    for incoming_ward in region.wards:
        # Check if this specific ward exists
        existing_ward = (
            db.query(WardDB)
            .filter(WardDB.region_id == db_region.id, WardDB.ward_id == incoming_ward.ward_id)
            .first()
        )

        # If it exists, delete it and its plots
        if existing_ward:
            for plot in existing_ward.plots:
                db.delete(plot)
            db.delete(existing_ward)
            db.commit()

    # Insert new wards and plots
    for ward in region.wards:
        db_ward = WardDB(ward_id=ward.ward_id, region=db_region)
        db.add(db_ward)
        db.commit()
        db.refresh(db_ward)

        for idx, plot in enumerate(ward.plots, start=1):
            db_plot = PlotDB(
                plot_number=plot.plot_number,
                price=plot.price,
                size=plot.size,
                available=plot.available,
                ward=db_ward,
                tenant_type = plot.tenant_type,
            )
            db.add(db_plot)
        db.commit()

    return {"status": "ok", "received": region.region_name}
