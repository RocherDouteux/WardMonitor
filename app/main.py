from fastapi import FastAPI
from app.models import Region
from app.logger import logger

app = FastAPI(title="WardMonitor", version="1.0")

@app.post("/ward-update")
async def receive_region(region: Region):
    logger.info(f"Received data for region: {region.region_name}")
    for ward in region.wards:
        logger.info(f"  Ward {ward.ward_id} with {len(ward.plots)} plots")
        for idx, plot in enumerate(ward.plots, start=1):
            logger.info(f"    Plot {idx:02}: {plot.size} - {plot.price:,} gil")
    return {"status": "ok", "received": region.region_name}
