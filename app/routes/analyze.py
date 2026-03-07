from http.client import HTTPException
from fastapi import APIRouter, Depends, Request
from app.services.data_collector import collect_market_data
from app.services.gemini_service import analyze_sector_with_gemini
from app.services.report_generator import generate_markdown_report
from app.security.auth import verify_api_key
from app.security.rate_limit import limiter
from app.security.session_tracker import track_session

router=APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request:Request,
    sector:str,
    api_key: str = Depends(verify_api_key)
    ):
    if len(sector) < 3:
        raise HTTPException(
            status_code=400,
            detail="Sector name too short"
        )
    else:
         # Track session usage
        session_count = track_session(request.client.host)
        market_data=collect_market_data(sector)
        analysis=analyze_sector_with_gemini(sector,market_data)
        report=generate_markdown_report(sector,analysis)
    return {"sector":sector,"message":report,"session_requests": session_count}