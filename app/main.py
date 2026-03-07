from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler


app = FastAPI(
    title="Trade Opportunities API",
    description="API for analyzing sector trade opportunities in India.",
    version="1.0"
)
from app.security.rate_limit import limiter
from app.routes.analyze import router as analyze_router

app.state.limiter=limiter
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(analyze_router)