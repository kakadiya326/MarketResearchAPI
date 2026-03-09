from datetime import datetime
import os

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
    
    os.makedirs("reports", exist_ok=True)

    # remove exatra space and signs
    remove_chars = [" ", "-", "_", "$", "  ", "/", "\\", "&"]

    for char in remove_chars:
        sector = sector.replace(char, "")

    filename=sector+"_"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_path = f"reports/{filename}_report.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

    return report