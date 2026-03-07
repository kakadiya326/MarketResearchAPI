from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title="Trade Opportunities API",
    description="API for analyzing sector trade opportunities in India.",
    version="1.0"
)

app.include_router(analyze_router)