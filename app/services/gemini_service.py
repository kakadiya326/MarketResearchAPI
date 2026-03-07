import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def analyze_sector_with_gemini(sector: str, market_data: str):

    try:

        prompt = f"""
            You are a financial analyst.

            Analyze the Indian {sector} sector.

            Provide:

            1. Market Overview
            2. Recent Developments
            3. Trade Opportunities
            4. Risks
            5. Investment Outlook

            Market Data:
            {market_data}
            """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"AI analysis failed: {str(e)}"