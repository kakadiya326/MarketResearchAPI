from datetime import datetime


def generate_markdown_report(sector: str, analysis: str):

    report = f"""
        # Trade Opportunity Report: {sector.title()} Sector (India)

        Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        ---

        {analysis}

        ---

        ## Data Source
        Market information collected from web search results and analyzed using Gemini AI.
        """

    return report