from fastapi import Header, HTTPException
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header(...)):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API Key"
        )

    return x_api_key