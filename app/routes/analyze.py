from http.client import HTTPException

from fastapi import APIRouter

from app.services.data_collector import collect_market_data
from app.services.gemini_service import analyze_sector_with_gemini

router=APIRouter()

@router.get("/analyze/{sector}")
async def analyze_sector(sector:str):
    if len(sector) < 3:
        raise HTTPException(
            status_code=400,
            detail="Sector name too short"
        )
    else:
        market_data=collect_market_data(sector)
        analysis=analyze_sector_with_gemini(sector,market_data)
    return {"sector":sector,"message":analysis}