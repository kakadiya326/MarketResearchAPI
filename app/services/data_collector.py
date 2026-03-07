from duckduckgo_search import DDGS


def search_sector_news(sector: str):

    query = f"India {sector} sector market news"

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=5)

        for r in search_results:
            results.append({
                "title": r["title"],
                "body": r["body"],
                "link": r["href"]
            })

    return results


def prepare_context(results):

    context = ""

    for item in results:

        context += f"""
Title: {item['title']}
Summary: {item['body']}
Source: {item['link']}

"""

    return context


def collect_market_data(sector: str):

    try:
        news_results = search_sector_news(sector)

        context = prepare_context(news_results)

        return context

    except Exception as e:

        return f"Error collecting data: {str(e)}"