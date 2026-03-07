from http.client import HTTPException

from fastapi import APIRouter

router=APIRouter()

@router.get("/analyze/{sector}")
async def analyze_sector(sector:str):
    if len(sector) < 3:
        raise HTTPException(
            status_code=400,
            detail="Sector name too short"
        )
    return {"sector":sector,"message":"API working"}